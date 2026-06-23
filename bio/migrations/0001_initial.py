from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="Your full name", max_length=100)),
                (
                    "job_title",
                    models.CharField(
                        help_text="e.g. Web Developer, CS Student", max_length=150
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        help_text="Upload your profile photo (stored in media/bio/)",
                        upload_to="bio/",
                    ),
                ),
                (
                    "professional_description",
                    models.TextField(
                        help_text="Short professional summary shown in About section"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, help_text="Contact email for footer", max_length=254
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, help_text="Optional phone number", max_length=20
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, help_text="e.g. Lahore, Pakistan", max_length=100
                    ),
                ),
            ],
            options={
                "verbose_name": "Bio",
                "verbose_name_plural": "Bio",
            },
        ),
    ]
