from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("edit/<str:entry>/", views.edit, name="edit"),
    path("search/", views.search, name="search"),
    path("<str:entry>/",views.strn,name='strn'),
    path("random/", views.rand, name="rand")
]
