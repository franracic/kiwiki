from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<str:entry>/",views.strn,name='strn'),
    path("random/", views.rand, name="rand")
]
