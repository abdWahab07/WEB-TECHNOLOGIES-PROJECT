from django.db import models


class Bio(models.Model):

    slug = models.SlugField(
        max_length=100,
        unique=True,
        default="abdul-wahab",
        help_text="URL-friendly identifier, e.g. abdul-wahab",
    )
    name = models.CharField(max_length=100, help_text="Your full name")
    job_title = models.CharField(
        max_length=150, help_text="e.g. Web Developer, CS Student"
    )
    profile_picture = models.ImageField(
        upload_to="bio/",
        blank=True,
        null=True,
        help_text="Upload your profile photo (stored in media/bio/)",
    )
    professional_description = models.TextField(
        help_text="Short professional summary shown in About section"
    )
    email = models.EmailField(blank=True, help_text="Contact email for footer")
    phone = models.CharField(
        max_length=20, blank=True, help_text="Optional phone number"
    )
    location = models.CharField(
        max_length=100, blank=True, help_text="e.g. Lahore, Pakistan"
    )
    linkedin = models.URLField(blank=True, help_text="LinkedIn profile URL")
    github = models.URLField(blank=True, help_text="GitHub profile URL")

    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bio"

    def __str__(self):
        return self.name

    @property
    def initials(self):
        parts = self.name.split()
        if not parts:
            return ""
        if len(parts) == 1:
            return parts[0][:1].upper()
        return f"{parts[0][:1]}{parts[-1][:1]}".upper()
