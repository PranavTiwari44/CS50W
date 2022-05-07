from django.urls import path

from . import views

app_name = "smartFridge"
urlpatterns = [
    path("", views.index, name="index")
]
