from django.shortcuts import render

from .models import Experience


def experience_section(request):

    experience_list = Experience.objects.all()
    return render(
        request,
        "experience/experience_section.html",
        {"experience_list": experience_list},
    )
