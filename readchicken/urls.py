from django.urls import path

from . import views

urlpatterns = [
    path("showchicken/", views.showchicken, name="readchicken/"),
]