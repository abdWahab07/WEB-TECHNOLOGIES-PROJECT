from django.contrib import admin

from .models import Bio


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "job_title", "email")
    search_fields = ("name", "slug", "job_title")
    prepopulated_fields = {"slug": ("name",)}
