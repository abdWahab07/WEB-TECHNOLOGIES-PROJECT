from django.urls import path

from . import views

urlpatterns = [
    path("", views.bio_section, name="bio_section"),
]
