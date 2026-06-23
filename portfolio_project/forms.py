from django import forms

from bio.models import Bio
from education.models import Education
from experience.models import Experience
from projects.models import Project
from skills.models import Skill

FORM_CONTROL = "form-control"


class StyledModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.setdefault("class", "form-check-input")
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.setdefault("class", "form-control form-select")
            else:
                field.widget.attrs.setdefault("class", FORM_CONTROL)


class BioForm(StyledModelForm):
    class Meta:
        model = Bio
        fields = [
            "slug",
            "name",
            "job_title",
            "profile_picture",
            "professional_description",
            "email",
            "phone",
            "location",
            "linkedin",
            "github",
        ]
        widgets = {
            "professional_description": forms.Textarea(attrs={"rows": 4}),
        }


class EducationForm(StyledModelForm):
    class Meta:
        model = Education
        fields = ["degree", "institute_name", "start_year", "end_year", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class SkillForm(StyledModelForm):
    class Meta:
        model = Skill
        fields = ["skill_name", "skill_category", "proficiency_level"]


class ExperienceForm(StyledModelForm):
    class Meta:
        model = Experience
        fields = ["role_title", "organization", "start_date", "end_date", "description"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class ProjectForm(StyledModelForm):
    class Meta:
        model = Project
        fields = [
            "project_title",
            "project_description",
            "technologies_used",
            "project_link",
        ]
        widgets = {
            "project_description": forms.Textarea(attrs={"rows": 3}),
        }
