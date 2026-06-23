from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("project_title", models.CharField(max_length=200)),
                ("project_description", models.TextField()),
                (
                    "technologies_used",
                    models.CharField(
                        help_text="Comma-separated list, e.g. Django, HTML, CSS, JavaScript",
                        max_length=300,
                    ),
                ),
                (
                    "project_link",
                    models.URLField(
                        blank=True, help_text="Live demo or GitHub repository URL"
                    ),
                ),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
                "ordering": ["-id"],
            },
        ),
    ]
