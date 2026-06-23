from django.shortcuts import render

from .models import Skill


def skills_section(request):

    skills_list = Skill.objects.all()
    return render(request, "skills/skills_section.html", {"skills_list": skills_list})
