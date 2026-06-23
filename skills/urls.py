from django.urls import path

from . import views

urlpatterns = [
    path("", views.skills_section, name="skills_section"),
]
