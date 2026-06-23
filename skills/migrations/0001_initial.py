from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skill",
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
                ("skill_name", models.CharField(max_length=100)),
                (
                    "skill_category",
                    models.CharField(
                        help_text="e.g. Programming, Frameworks, Tools", max_length=100
                    ),
                ),
                (
                    "proficiency_level",
                    models.CharField(
                        choices=[
                            ("beginner", "Beginner"),
                            ("intermediate", "Intermediate"),
                            ("advanced", "Advanced"),
                            ("expert", "Expert"),
                        ],
                        default="intermediate",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "Skill",
                "verbose_name_plural": "Skills",
                "ordering": ["skill_category", "skill_name"],
            },
        ),
    ]
