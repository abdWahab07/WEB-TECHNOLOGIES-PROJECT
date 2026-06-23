from bio.models import Bio
from education.models import Education
from experience.models import Experience
from projects.models import Project
from skills.models import Skill

from .portfolio_utils import get_active_portfolio


def portfolio_context(request):
    portfolio = get_active_portfolio(request)
    if not portfolio:
        return {
            "bio": None,
            "portfolios": Bio.objects.all(),
            "home_prefix": "",
            "has_education": False,
            "has_skills": False,
            "has_experience": False,
            "has_projects": False,
        }

    return {
        "bio": portfolio,
        "portfolios": Bio.objects.all(),
        "home_prefix": "/laiba" if portfolio.slug == "laiba-zainab" else "",
        "has_education": Education.objects.filter(portfolio=portfolio).exists(),
        "has_skills": Skill.objects.filter(portfolio=portfolio).exists(),
        "has_experience": Experience.objects.filter(portfolio=portfolio).exists(),
        "has_projects": Project.objects.filter(portfolio=portfolio).exists(),
    }
