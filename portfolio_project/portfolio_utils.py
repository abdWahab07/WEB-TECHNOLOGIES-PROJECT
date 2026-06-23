from bio.models import Bio

DEFAULT_PORTFOLIO_SLUG = "abdul-wahab"


def get_active_portfolio(request):
    slug = request.GET.get("portfolio") or request.session.get(
        "portfolio_slug", DEFAULT_PORTFOLIO_SLUG
    )
    portfolio = Bio.objects.filter(slug=slug).first()
    if not portfolio:
        portfolio = Bio.objects.order_by("id").first()
    if portfolio:
        request.session["portfolio_slug"] = portfolio.slug
    return portfolio
