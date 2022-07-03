import django_tables2 as tables
from .models import *
from django.apps import apps

class AdjazenzTable(tables.Table):
    class Meta:
        model = adjazenzmatrix_variablen
        template_name = "django_tables2/bootstrap.html"


class BeziehungenTable(tables.Table):
    class Meta:
        model = beziehungen_variablen
        template_name = "django_tables2/bootstrap.html"


class BrennerOZ1Table(tables.Table):
    class Meta:
        model = brenner_ofenzone_1
        template_name = "django_tables2/bootstrap.html"


class BrennerOZ2Table(tables.Table):
    class Meta:
        model = brenner_ofenzone_2
        template_name = "django_tables2/bootstrap.html"


class BrennerOZ3Table(tables.Table):
    class Meta:
        model = brenner_ofenzone_3
        template_name = "django_tables2/bootstrap.html"


class IstwerteTable(tables.Table):
    class Meta:
        model = istwerte
        template_name = "django_tables2/bootstrap4.html"


class KonvektivZoneTable(tables.Table):
    class Meta:
        model = konvektivzone
        template_name = "django_tables2/bootstrap.html"


class Ofenzone1Table(tables.Table):
    class Meta:
        model = ofenzone_1
        template_name = "django_tables2/bootstrap.html"


class Ofenzone2Table(tables.Table):
    class Meta:
        model = ofenzone_2
        template_name = "django_tables2/bootstrap.html"


class Ofenzone3Table(tables.Table):
    class Meta:
        model = ofenzone_3
        template_name = "django_tables2/bootstrap.html"


class Ofenzone4Table(tables.Table):
    class Meta:
        model = ofenzone_4
        template_name = "django_tables2/bootstrap.html"


class RekuperatorTable(tables.Table):
    class Meta:
        model = rekuperator
        template_name = "django_tables2/bootstrap.html"


class RestwerteTable(tables.Table):
    class Meta:
        model = restwerte
        template_name = "django_tables2/bootstrap.html"
