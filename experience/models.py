from django.db import models


class Experience(models.Model):

    portfolio = models.ForeignKey(
        "bio.Bio",
        on_delete=models.CASCADE,
        related_name="experiences",
        null=True,
        blank=True,
    )
    role_title = models.CharField(max_length=200, help_text="Job title or role")
    organization = models.CharField(
        max_length=200, help_text="Company or organization name"
    )
    start_date = models.DateField(help_text="When you started this role")
    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="End date (leave empty if current job)",
    )
    description = models.TextField(help_text="What you did in this role")

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.role_title} at {self.organization}"

    @property
    def is_current(self):
        return self.end_date is None

    @property
    def date_range(self):

        start = self.start_date.strftime("%b %Y")
        end = "Present" if self.is_current else self.end_date.strftime("%b %Y")
        return f"{start} – {end}"
