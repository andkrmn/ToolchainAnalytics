import numpy as np
import pandas as pd

def create_nan(df, percentage):

    import random

    control_variable = 0

    no_variables = int(len(df.columns))
    no_index = len(df.index)
    no_datapoints = int(len(df.index)*no_variables * percentage)

    print("Anzahl an Variablen: ", no_variables)
    print("Anzahl Datenpunkte, die manipuliert werden sollen: ", no_datapoints)

    tracking_nans = np.zeros((no_index, no_variables))
    tracking_variable = 0

    while control_variable < no_datapoints:

        # Errechne zufällige Variable
        idx_variable = random.randrange(no_variables)
        variable = df.columns[idx_variable]
        #print("Zufallsvariable: ", variable)

        # Errechne zufälligen Zeitschritt
        idx_index = random.randrange(no_index)
        #print("Zufallsindex: ", idx_index)

        if tracking_nans[idx_index, idx_variable] == np.nan:
            print("Datenpunkt ist bereits NAN!")

        tracking_nans[idx_index, idx_variable] = np.nan
        tracking_variable = tracking_variable + 1

        # manipuliere Wert in Dataframe
        df[variable].iloc[idx_index] = np.nan
        control_variable = control_variable + 1

    data = [no_variables, no_datapoints]
    return df, data


def replace_nans(df_nan):
    '''
    score1: anzahl nan werte / anzahl gesammt messwerte
    score2: anzahl nan aneinderfolgend

    '''

    log_file = {}
    scores = {}
    logger = {}

    for variable in df_nan.columns:

        df = df_nan[[variable]]  # wichtig ist, dass es sich um dataframe handelt

        score = 0

        # 0. neuer Index: Zeitstamps wenig aussagekräft, deshalb lieber fortlaufender index

        index_new = np.arange(len(df))
        df = df.set_index(index_new)
        indices_nan = []

        # 1. Hat variable nan Wert, wenn ja wie viele ?

        if df[df.columns[0]].isnull().any() == True:  # if-Schleife, die prüft ob Nan Werte enthalten sind
            summe = df[df.columns[0]].isnull().sum()
            df['NaN'] = df[df.columns[0]].isnull()
            print(f"Variable {variable} weißt {summe} NaN Werte auf!")
            score = round(summe / len(df), 3)
            print(f"Dies entspricht einem Anteil von {score}")
            logger[f"{variable}"] = summe

        else:
            print(f'Variable {variable} enthält keine NaN Werte!')
            continue

        # 2. Gebe Indices der Nan Werte an

        indices_nan = df.index[df['NaN'] == True].tolist()

        # 3. Gibt es benachbarte NaN-Werte ?

        score2 = 0
        indices_nan_row = []

        for indice in indices_nan:

            # check if indice is alread in indices_nan_row
            if indice in indices_nan_row:
                # print("Index wurde bereits erkannt")
                continue

            # überprüfe die anzahl an nachbarn der indices
            for k in range(1, 10):
                if (indice + k) in indices_nan:
                    # print(f"Indice {indice+k} ist direkt benachbart zu {indice}")
                    indices_nan_row.append(indice)
                    score2 = score2 + 10 * k

                else:
                    # print(f"Indice {indice} hat keine direkt benachbarten NaN Werte")
                    break

            # print(f"Der Score beträgt: {score2}")

        score_var = round((score2 + score) / len(df), 3)
        print(f"Der Score der Variable {variable} beträgt: ", score_var)

        # 3. Ersetze Nan Werte durch Mittelwert
        # Wenn score_var > .2 sollten die Werte nicht mer durch Mittelwert ersetzt werden, weil
        # strukturelles Problem vorliegt!

        if score_var < .3:
            # berechne mittelwert
            mean = df.describe().mean()
            # ersetze werte
            df = df.fillna(method='bfill')
            # ersetze Wert in dataframe
            df_nan.loc[:, variable] = df[variable].values

        else:
            print("Score zu groß! Es liegt ein strukturelles Problem vor.")

        # 5. Gebe Log-File mit Indices der Nan Werte aus
        log_file[variable] = indices_nan
        scores[variable] = score_var

    print(logger)
    return df_nan, log_file, scores, logger


def check_datatype(df):
    '''
    Input: Dataframe Objekt
    Output: Ausgabe der verfügbaren Datentypen
    '''
    datentypen = df.dtypes.unique()
    print("Folgende Datentypen liegen vor: ", datentypen)

    return datentypen


def seperate_data(df, int_variables=None):
    '''
    Auftrennung in numerische und kategorische Variablen.
    Wenn keine integer Variablen angegeben sind, werden nur numerische und kategorische
    Variablen zurückgegeben.
    input: df --> Dataframe;
        int_variables --> list of strings
    output: df_float --> Dataframe
            df_categorical --> Dataframe
    '''

    df_float = df.select_dtypes(include=['float64'])
    df_categorical = df.select_dtypes(include=['int64'])
    df_int = df[['zaehler']]
    df_num = pd.concat([df_float, df_int], axis=1)
    df_categorical = df_categorical.drop(columns=['zaehler'])

    return df_num, df_categorical


def replace_outliers(df, heuristic):
    '''
    Diese Funktion entscheidet ob ein Wert ein Ausreißer Wert ist auf Grundlage der übergegeben Heuristik.
    Alle Werte, die die Bedingung gegeben durch die Heuristik nicht erfüllen werden durch NaN Werte ersetzt.
    Diese wiederum können durch die bereits existierenden Funktionen ersetzt werden. Außerdem bilden diese
    Funktionen erneut einen Score, der das Datensetz bewertet.
    '''
    # Werte werden mittels pandas ausgewählt
    units = {
        "temperature": ['tist_zone_1', 'tist_zone_2', 'tist_zone_3', 'tist_zone_4', 't_abgas_vor_kuehlluft',
                        't_abgas_regel_kuehlluft', 't_abgas_nach_reku', 't_abgas_nach_ventilator',
                        't_luft_vor_reku', 't_luft_nach_reku', 'tsoll_akt_zone_1', 'tsoll_akt_zone_2',
                        'tsoll_akt_zone_3', 'tsoll_akt_zone_4', 'tsoll_luft_ausblas', 'tsoll_abgas_kuehl',
                        'bl_eintragetemp'],
        "partial_pressure": ['o2_zone1', 'o2_zone2', 'o2_zone3', 'o2_zone4',
                             'o2_kvz', 'o2_vor_reku', 'o2_nach_reku', 'co_kvz'],
        "absolute_pressure": ['ofenraumdruck_zone_1', 'ofenraumdruck_zone_2', 'ofenraumdruck_zone_3',
                              'ofenraumdruck_zone_4'],
        "flow": ['f_luft_z1', 'f_luft_z2', 'f_luft_z3', 'f_luft_z4', 'f_gas_z1', 'f_gas_z2', 'f_gas_z3',
                 'f_gas_z4']}
    for key in list(units.keys()):
        # select heuristic
        interval_right = heuristic[key][1]
        interval_left = heuristic[key][0]
        # select all variables
        variables = units[key]
        # loop over variables
        for variable in variables:
            # replace values that do not fullfill the condition with nan values
            df[variable].where(df[variable] < interval_right, np.nan, inplace=True)
            df[variable].where(df[variable] > interval_left, np.nan, inplace=True)

        return df


def one_hot_encoding(df, variables='all'):
    # one hot encoding für alle variablen
    if variables == 'all':
        print("One-Hot-Encoding von allen Variablen")

        # anzahl der jeweiligen klassen
        n_classes = df.nunique()

        # schleife über alle variablen
        for variable in df.columns:
            # print(variable)
            # one hot encoding
            one_hot = pd.get_dummies(df[variable], prefix=variable)  # pd dummies von pd.series objekt!!!
            # zusammenbringen des alten dataframes mit encoded dataframe
            df = pd.concat([df, one_hot], axis=1)
            # löschen der obsoleten variablen
            df = df.drop(variable, axis=1)

        return n_classes, df

    elif type(variables) == str:
        print(f"One-Hot-Encoding der Variable {variables}")
        df = df[variables]
        n_classes = df.nunique()
        one_hot = pd.get_dummies(df, prefix=variables)
        df = pd.concat([df, one_hot], axis=1)
        df = df.drop(variables, axis=1)
        return n_classes, df

    elif type(variables) == list:
        print(f"One-Hot-Encoding mehrerer Variablen {variables}")
        df = df[variables]
        n_classes = df.nunique()
        for variable in df.columns:
            one_hot = pd.get_dummies(df[variable], prefix=variable)
            df = pd.concat([df, one_hot], axis=1)
            df = df.drop(variable, axis=1)
            return n_classes, df


def combine_data(df_num, df_cat):
    return pd.concat([df_num, df_cat], axis = 1)


def test_train_split(df_new, split, shuffle=False):
    # Dataframe to numpy
    X_ges = df_new.to_numpy()

    # Shuffle Data
    if shuffle == True:
        np.random.shuffle(X_ges)

    # Daten splitten
    split = split
    index = round(len(X_ges) * split)

    X_train = X_ges[:-index]
    X_test = X_ges[-index:]

    return X_train, X_test


def transform_datetimeindex(df, variable_datetime, format = None):
    '''
    Funktion transformiert angegeben datetime Variable
    Format: '%Y-%m-%d %H:%M:%S'
    Input: df --> Dataframe
        variable_datetime --> String

    Output df --> Dataframe
    '''
    variable_datetime = 'toi'

    if format == None:
        format = '%Y-%m-%d %H:%M:%S'

    time = pd.to_datetime(df[variable_datetime])  # am Ende muss series erhalten werden
    time = time.dt.strftime(format)  # Ändere Format
    time = pd.DatetimeIndex(time)
    df = df.set_index(time)
    df = df.drop(columns=['toi'])

    return df


def time_intervall(df):
    start = pd.to_datetime(df.index[0])
    end = pd.to_datetime(df.index[[-1]])

    delta = end - start

    def complete_hours(delta):
        return (delta.components.days * 24 + delta.components.hours)

    hours = complete_hours(delta)

    return hours


# def scaling(X_train, X_test, MinMaxScaling=True):
#
#
#     if MinMaxScaling == True:
#         scaler = MinMaxScaler()
#     else:
#         sclaer = StandardScaler()
#
#     X_train = scaler.fit_transform(X_train)
#     X_test = scaler.fit_transform(X_test)
#
#     return X_train, X_test