import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import psycopg2
from psycopg2 import Error
from django.apps import apps
from .preprocess_functions import *


mumerical_variables = {
    'Temperatur Ofen': ['tist_zone_1', 'tist_zone_2', 'tist_zone_3', 'tist_zone_4', "Temperatur"],
    'Temperatur Außerhalb':  ['t_abgas_vor_kuehlluft', 't_abgas_regel_kuehlluft', 't_abgas_nach_reku',
                        't_abgas_nach_ventilator', 't_luft_vor_reku', 't_luft_nach_reku', "Temperatur"],
    'O2 Gehalt Ofen': ['o2_zone1', 'o2_zone2', 'o2_zone3', 'o2_zone4', 'o2_kvz', "O2 Gehalt"],
    'O2 Gehalt Peripherie':  ['o2_vor_reku', 'o2_nach_reku', "O2 Gehalt"],
    'CO Gehalt Ofen':  ['co_kvz', "CO Gehalt"],
    'Druck Ofen':  ['ofenraumdruck_zone_1', 'ofenraumdruck_zone_2','ofenraumdruck_zone_3', 'ofenraumdruck_zone_4', "Druck"],
    'Volumenstrom Verbrennungsluft':['f_luft_z1', 'f_luft_z2', 'f_luft_z3', 'f_luft_z4', "Volumenstrom"],
    'Volumenstrom Brenngas':  ['f_gas_z1', 'f_gas_z2', 'f_gas_z3', 'f_gas_z4', "Volumenstrom"],
    'Temperatur Sollwerte': ['tsoll_akt_zone_1', 'tsoll_akt_zone_2','tsoll_akt_zone_3', 'tsoll_akt_zone_4',
                   'tsoll_luft_ausblas', 'tsoll_abgas_kuehl', "Temperatur"],
    'Variablen Umgebung': ['bl_eintragetemp', "Temperatur"]
}


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf8")
    buffer.close()
    return graph


def get_df():
    model = apps.get_model("toolchain", "istwerte")
    item = model.objects.all().values()
    dataframe = pd.DataFrame(item)
    return dataframe


def prepare_df(df):
    variable_datetime = 'toi'
    df = transform_datetimeindex(df, variable_datetime)
    all_data = df.sort_index()
    start = pd.to_datetime(all_data.index[[0]])
    print(start)
    end = pd.to_datetime(all_data.index[[-1]])
    print(end)
    delta = end - start
    print(delta)
    heuristic = {
        "temperature": [0, 1600],
        "partial_pressure": [0, 100],
        "absolute_pressure": [0, 1],
        "flow": [0, 2500]
    }
    df_num = seperate_data(df)[0]
    df = replace_outliers(df_num, heuristic)
    df_new, log_file, scores, logger = replace_nans(df)
    df_new.sort_index()
    df["toi"] = df.index
    print(list(df_new))
    return df_new


def get_intervall(df):
    hours = time_intervall(df)
    return hours


def get_plot(key1, key2, plot_type):

    df = prepare_df(get_df())
    hours = get_intervall(df)
    columns = mumerical_variables[key1]
    columns2 = mumerical_variables[key2]

    if plot_type == "Time Plot":
        x = df["toi"].to_list()
        # y = df["tist_zone_1"].to_list()
        plt.switch_backend("AGG")
        plt.figure(figsize=(10, 5))
        plt.title("Time Plot")

        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        for y in columns[:-1]:
            y = df[y].to_list()
            ax1.plot(x, y)
        y_axis1 = columns[-1]
        for y in columns2[:-1]:
            y = df[y].to_list()
            ax2.plot(x, y)
        y_axis2 = columns2[-1]
        ax1.set_xlabel("Date")
        ax1.set_ylabel(y_axis1)
        ax2.set_ylabel(y_axis2)
        plt.tight_layout()

    if plot_type == "Box Plot":
        plt.switch_backend("AGG")
        plt.figure(figsize=(10, 5))
        plt.title("Box Plot")
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        all1 = []
        for y in columns[:-1]:
            y = df[y].to_list()
            all1.append(y)
        # ax1.boxplot(all1)
        y_axis1 = columns[-1]
        all2 = []
        for y in columns2[:-1]:
            y = df[y].to_list()
            all1.append(y)
        ax1.boxplot(all1)
        y_axis2 = columns2[-1]
        ax1.set_ylabel(y_axis1)
        ax2.set_ylabel(y_axis2)
        plt.tight_layout()

        # for y in columns[:-1]:
        #     y = df[y].to_list()
        #     ax.boxplot(y)
        # y_axis1 = columns[-1]
        # ax.set_ylabel(y_axis1)
        # plt.tight_layout()

    if plot_type == "Heatmap Plot":
        plt.switch_backend("AGG")
        plt.figure(figsize=(10, 5))
        plt.title("Heatmap Plot")


    graph = get_graph()

    return graph, hours


def connect_database(hostname, database_name, user, pwd, port):
    hostname = hostname
    database_name = database_name
    username = user
    pwd = pwd
    port = port

    try:
        conn = psycopg2.connect(
            host=hostname,
            port=5432,
            database=database_name,
            user=username,
            password=pwd)
    except (Exception, Error) as error:
        print("Verbingung konnte nicht hergestellt werden, bitte überprüfen Sie Ihre Eingabedaten!", error)

    else:
        print("Die Verbingung mit PostgreSQL war erfolgreich! ")

    cur = conn.cursor()

    return cur


def close_connection(cur, conn):
    cur.close()
    conn.close()
    return


def sql_query(cur, sql):
    cur.execute(sql)
    rs = cur.fetchall()
    return rs


def get_tables(cur):
    tables = []
    cur.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'public'""")
    for table in cur.fetchall():
        tables.append(table)
    return tables

