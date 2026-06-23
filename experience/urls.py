from django.urls import path

from . import views

urlpatterns = [
    path("", views.experience_section, name="experience_section"),
]
