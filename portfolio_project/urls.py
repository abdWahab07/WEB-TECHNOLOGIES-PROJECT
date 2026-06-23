from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from . import views

admin.site.site_header = "Portfolio Admin Panel"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage Portfolio Content"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("portfolio/<slug:slug>/", views.switch_portfolio, name="switch_portfolio"),
    path("createPortfolio/", views.create_portfolio, name="create_portfolio"),
    path("bio/", include("bio.urls")),
    path("education/", include("education.urls")),
    path("skills/", include("skills.urls")),
    path("experience/", include("experience.urls")),
    path("projects/", include("projects.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]
