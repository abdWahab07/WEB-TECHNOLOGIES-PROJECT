from django.shortcuts import render

from .models import Project


def projects_section(request):

    projects_list = Project.objects.all()
    return render(
        request, "projects/projects_section.html", {"projects_list": projects_list}
    )
