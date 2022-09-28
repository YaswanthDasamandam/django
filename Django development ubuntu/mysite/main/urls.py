from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>",views.index,name="index"),
    path("<str:name>",view=views.index_name,name="index"),
    path("",views.home,name = "Home"),
]