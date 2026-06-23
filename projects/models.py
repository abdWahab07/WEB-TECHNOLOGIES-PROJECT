from django.db import models


class Project(models.Model):

    portfolio = models.ForeignKey(
        "bio.Bio",
        on_delete=models.CASCADE,
        related_name="projects",
        null=True,
        blank=True,
    )
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    technologies_used = models.CharField(
        max_length=300,
        help_text="Comma-separated list, e.g. Django, HTML, CSS, JavaScript",
    )
    project_link = models.URLField(
        blank=True,
        help_text="Live demo or GitHub repository URL",
    )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-id"]

    def __str__(self):
        return self.project_title

    @property
    def technology_list(self):

        return [
            tech.strip() for tech in self.technologies_used.split(",") if tech.strip()
        ]
