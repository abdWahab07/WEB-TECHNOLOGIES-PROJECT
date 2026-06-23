from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
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
                (
                    "degree",
                    models.CharField(
                        help_text="Degree or qualification name", max_length=200
                    ),
                ),
                (
                    "institute_name",
                    models.CharField(
                        help_text="University or school name", max_length=200
                    ),
                ),
                (
                    "start_year",
                    models.PositiveIntegerField(
                        help_text="Year studies started, e.g. 2022"
                    ),
                ),
                (
                    "end_year",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Year completed (leave empty if ongoing)",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Optional details about this degree"
                    ),
                ),
            ],
            options={
                "verbose_name": "Education",
                "verbose_name_plural": "Education",
                "ordering": ["-start_year"],
            },
        ),
    ]
