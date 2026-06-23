from django.shortcuts import render

from .models import Education


def education_section(request):

    education_list = Education.objects.all()
    return render(
        request, "education/education_section.html", {"education_list": education_list}
    )
