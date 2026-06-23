from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from bio.models import Bio
from education.models import Education
from experience.models import Experience
from projects.models import Project
from skills.models import Skill

from .forms import BioForm, EducationForm, ExperienceForm, ProjectForm, SkillForm
from .portfolio_utils import get_active_portfolio


def home(request):
    return _render_portfolio(request, "abdul-wahab")


def laiba_home(request):
    return _render_portfolio(request, "laiba-zainab")


def switch_portfolio(request, slug):
    portfolio = get_object_or_404(Bio, slug=slug)
    return redirect(portfolio.home_url)


def _render_portfolio(request, slug):
    request.session["portfolio_slug"] = slug
    portfolio = Bio.objects.filter(slug=slug).first() or Bio.objects.first()
    home_prefix = "/laiba" if portfolio and portfolio.slug == "laiba-zainab" else ""

    context = {
        "bio": portfolio,
        "portfolios": Bio.objects.all(),
        "home_prefix": home_prefix,
        "education_list": Education.objects.filter(portfolio=portfolio),
        "skills_list": Skill.objects.filter(portfolio=portfolio),
        "experience_list": Experience.objects.filter(portfolio=portfolio),
        "projects_list": Project.objects.filter(portfolio=portfolio),
    }
    return render(request, "home.html", context)


@staff_member_required
def create_portfolio(request):
    portfolio = get_active_portfolio(request)
    bio_form = BioForm(instance=portfolio)
    education_form = EducationForm()
    skill_form = SkillForm()
    experience_form = ExperienceForm()
    project_form = ProjectForm()

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "bio":
            bio_form = BioForm(request.POST, request.FILES, instance=portfolio)
            if bio_form.is_valid():
                bio_form.save()
                messages.success(request, "Bio saved successfully.")
                return redirect("create_portfolio")

        elif form_type == "education":
            education_form = EducationForm(request.POST)
            if education_form.is_valid():
                record = education_form.save(commit=False)
                record.portfolio = portfolio
                record.save()
                messages.success(request, "Education record added.")
                return redirect("create_portfolio")

        elif form_type == "skill":
            skill_form = SkillForm(request.POST)
            if skill_form.is_valid():
                record = skill_form.save(commit=False)
                record.portfolio = portfolio
                record.save()
                messages.success(request, "Skill added.")
                return redirect("create_portfolio")

        elif form_type == "experience":
            experience_form = ExperienceForm(request.POST)
            if experience_form.is_valid():
                record = experience_form.save(commit=False)
                record.portfolio = portfolio
                record.save()
                messages.success(request, "Experience record added.")
                return redirect("create_portfolio")

        elif form_type == "project":
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                record = project_form.save(commit=False)
                record.portfolio = portfolio
                record.save()
                messages.success(request, "Project added.")
                return redirect("create_portfolio")

        messages.error(request, "Please fix the errors below and try again.")

    context = {
        "bio": portfolio,
        "portfolios": Bio.objects.all(),
        "bio_form": bio_form,
        "education_form": education_form,
        "skill_form": skill_form,
        "experience_form": experience_form,
        "project_form": project_form,
        "education_list": Education.objects.filter(portfolio=portfolio),
        "skills_list": Skill.objects.filter(portfolio=portfolio),
        "experience_list": Experience.objects.filter(portfolio=portfolio),
        "projects_list": Project.objects.filter(portfolio=portfolio),
    }
    return render(request, "create_portfolio.html", context)
