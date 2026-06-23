from django.shortcuts import render

from .models import Bio


def bio_section(request):

    bio = Bio.objects.first()
    return render(request, "bio/bio_section.html", {"bio": bio})
