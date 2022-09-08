from django.urls import path
from . import views

urlpatterns = [
    path("",views.SystemInformations.as_view(),name="home"),
]