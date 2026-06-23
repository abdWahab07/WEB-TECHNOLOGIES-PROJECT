from django.db import models


class Education(models.Model):

    portfolio = models.ForeignKey(
        "bio.Bio",
        on_delete=models.CASCADE,
        related_name="education_records",
        null=True,
        blank=True,
    )
    degree = models.CharField(max_length=200, help_text="Degree or qualification name")
    institute_name = models.CharField(
        max_length=200, help_text="University or school name"
    )
    start_year = models.PositiveIntegerField(
        help_text="Year studies started, e.g. 2022"
    )
    end_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Year completed (leave empty if ongoing)",
    )
    description = models.TextField(
        blank=True, help_text="Optional details about this degree"
    )

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ["-start_year"]

    def __str__(self):
        return f"{self.degree} - {self.institute_name}"

    @property
    def year_range(self):

        if self.end_year:
            return f"{self.start_year} – {self.end_year}"
        return f"{self.start_year} – Present"
