from django.urls import path

from . import views

urlpatterns = [
    path("", views.education_section, name="education_section"),
]
