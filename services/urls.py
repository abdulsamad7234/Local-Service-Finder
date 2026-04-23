from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.service_list, name="service_list"),
    path("services/add/", views.service_create, name="service_create"),
    path("services/<int:pk>/<slug:slug>/", views.service_detail, name="service_detail"),
]
