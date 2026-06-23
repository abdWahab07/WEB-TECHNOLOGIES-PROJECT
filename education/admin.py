from django.contrib import admin

from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institute_name", "start_year", "end_year")
    list_filter = ("start_year",)
    search_fields = ("degree", "institute_name")
