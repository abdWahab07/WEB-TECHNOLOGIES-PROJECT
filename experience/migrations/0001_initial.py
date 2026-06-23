from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Experience",
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
                    "role_title",
                    models.CharField(help_text="Job title or role", max_length=200),
                ),
                (
                    "organization",
                    models.CharField(
                        help_text="Company or organization name", max_length=200
                    ),
                ),
                (
                    "start_date",
                    models.DateField(help_text="When you started this role"),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True,
                        help_text="End date (leave empty if current job)",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(help_text="What you did in this role"),
                ),
            ],
            options={
                "verbose_name": "Experience",
                "verbose_name_plural": "Experience",
                "ordering": ["-start_date"],
            },
        ),
    ]
