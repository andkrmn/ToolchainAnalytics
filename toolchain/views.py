from django.apps import apps
from django.shortcuts import render
from django.apps import apps
from .tables import *
from .models import *
from .forms import HeuristicForm
from .preprocess_functions import *
from .utils import get_plot


def get_isttable():
    model = apps.get_model("toolchain", "istwerte")
    item = model.objects.all().values()
    dataframe = pd.DataFrame(item)
    return dataframe


def start(request):
    return render(request, "toolchain/index.html")


def all_tables(request):
    # get models from database
    table_list = [m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()][6:]
    # create dict with {model: columns_list}
    # spalten = {}
    # for i, table in enumerate(table_list):
    #     table_model = apps.get_model("toolchain", table)
    #     name = [f.name for f in table_model._meta.get_fields()]
    #     spalten[table] = name
    # print(spalten)
    # # testweise istwerte mitgeben
    # istwerte_spalten = spalten["istwerte"]

    # istwerte table
    model1 = apps.get_model("toolchain", "istwerte")
    data1 = model1.objects.all()[:30]

    # beziehungen_variablen table
    model2 = apps.get_model("toolchain", "beziehungen_variablen")
    data2 = model2.objects.all()[:30]

    # brenner ofenzon_1
    model3 = apps.get_model("toolchain", "brenner_ofenzone_1")
    data3 = model3.objects.all()[:30]

    # brenner ofenzone 2
    model4 = apps.get_model("toolchain", "brenner_ofenzone_2")
    data4 = model4.objects.all()[:30]

    # brenner ofenzone 3
    model5 = apps.get_model("toolchain", "brenner_ofenzone_3")
    data5 = model5.objects.all()[:30]

    # konvektivzone
    model6 = apps.get_model("toolchain", "konvektivzone")
    data6 = model6.objects.all()[:30]

    # ofenzone_1
    model7 = apps.get_model("toolchain", "ofenzone_1")
    data7 = model7.objects.all()[:30]

    # ofenzone_2
    model8 = apps.get_model("toolchain", "ofenzone_2")
    data8 = model8.objects.all()[:30]

    # ofenzone_3
    model9 = apps.get_model("toolchain", "ofenzone_3")
    data9 = model9.objects.all()[:30]

    # ofenzone_4
    model10 = apps.get_model("toolchain", "ofenzone_4")
    data10 = model10.objects.all()[:30]

    # rekuperator
    model11 = apps.get_model("toolchain", "rekuperator")
    data11 = model11.objects.all()[:30]

    # restwerte
    model12 = apps.get_model("toolchain", "restwerte")
    data12 = model12.objects.all()[:30]

    return render(request, "toolchain/index.html", {"table_list": table_list, "data1": data1, "data2": data2,
                                                    "data3": data3, "data4": data4, "data5": data5, "data6": data6,
                                                    "data7": data7, "data8": data8, "data9": data9, "data10": data10,
                                                    "data11": data11, "data12": data12, })


def preprocessing(request):
    return render(request, "toolchain/preprocessing.html")


def replace_nan(request, tablename):
    print(tablename)
    return render(request, "toolchain/preprocessing0.html", {"tablename": tablename})


def split(request, tablename):
    return render(request, "toolchain/preprocessing1.html", {"tablename": tablename})


def get_heuristic(request, tablename):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HeuristicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            heuristic = {
                "temperature": [form.cleaned_data["tempmin"], form.cleaned_data["tempmax"]],
                "partial_pressure": [form.cleaned_data["partialpressuremin"], form.cleaned_data["partialpressuremax"]],
                "absolute_pressure": [form.cleaned_data["absolutepressuremin"],
                                      form.cleaned_data["absolutepressuremax"]],
                "flow": [form.cleaned_data["flowmin"], form.cleaned_data["flowmax"]]
            }
            df = get_isttable()
            df_num = seperate_data(df)[0]
            df_heuristic = df_num.copy()
            df_nan = replace_outliers(df_heuristic, heuristic)
            df_new, log_file, scores, logger = replace_nans(df_nan)
            outliers_nmbr = logger
            return render(request, 'toolchain/preprocessing3.html', {'form': form, "tablename": tablename,
                                                                    "outliers_nmbr": outliers_nmbr})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HeuristicForm()

    return render(request, "toolchain/preprocessing2.html", {'form': form, "tablename": tablename})


def machine_learning(request, tablename):
    return render(request, "toolchain/preprocessing4.html", {"tablename": tablename})


def visualisation(request):
    return render(request, "toolchain/visualisation.html")


def plots(request, tablename):
    # chart, intervall = get_plot()
    return render(request, "toolchain/visualisation1.html")


def result(request):

    key1 = request.GET["key1"]
    key2 = request.GET["key2"]
    plot_type = request.GET["plot_type"]

    chart, intervall = get_plot(key1, key2, plot_type)

    # chart, intervall = get_plot()

    return render(request, "toolchain/visualisation1.html", {"chart": chart, "intervall": intervall})












