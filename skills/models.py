from django.db import models


class Skill(models.Model):

    portfolio = models.ForeignKey(
        "bio.Bio",
        on_delete=models.CASCADE,
        related_name="skills",
        null=True,
        blank=True,
    )
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

    PROFICIENCY_CHOICES = [
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, "Intermediate"),
        (ADVANCED, "Advanced"),
        (EXPERT, "Expert"),
    ]

    PROFICIENCY_PERCENT = {
        BEGINNER: 25,
        INTERMEDIATE: 50,
        ADVANCED: 75,
        EXPERT: 100,
    }

    skill_name = models.CharField(max_length=100)
    skill_category = models.CharField(
        max_length=100,
        help_text="e.g. Programming, Frameworks, Tools",
    )
    proficiency_level = models.CharField(
        max_length=20,
        choices=PROFICIENCY_CHOICES,
        default=INTERMEDIATE,
    )

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ["skill_category", "skill_name"]

    def __str__(self):
        return f"{self.skill_name} ({self.get_proficiency_level_display()})"

    @property
    def proficiency_percent(self):

        return self.PROFICIENCY_PERCENT.get(self.proficiency_level, 50)
