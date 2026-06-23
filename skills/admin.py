from django.contrib import admin

from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "skill_category", "proficiency_level")
    list_filter = ("skill_category", "proficiency_level")
    search_fields = ("skill_name", "skill_category")
