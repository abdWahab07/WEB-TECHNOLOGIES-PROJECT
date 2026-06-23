from django.contrib import admin

from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role_title", "organization", "start_date", "end_date")
    list_filter = ("organization",)
    search_fields = ("role_title", "organization")
