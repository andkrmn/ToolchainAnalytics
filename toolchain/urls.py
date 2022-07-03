from django.urls import path
from . import views


urlpatterns = [
    path("start", views.all_tables),
    path("preprocessing", views.preprocessing),
    path("preprocessing/<tablename>", views.replace_nan),
    path("preprocessing1/<tablename>", views.split),
    path("preprocessing2/<tablename>", views.get_heuristic),
    path("preprocessing4/<tablename>", views.machine_learning),
    path("visualisation", views.visualisation),
    path("visualisation/<tablename>", views.plots),
    path("result", views.result),

]
