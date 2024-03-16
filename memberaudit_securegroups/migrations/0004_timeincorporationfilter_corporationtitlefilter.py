# Generated by Django 4.2.10 on 2024-02-11 11:09

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0017_alliance_and_corp_names_are_not_unique"),
        ("memberaudit_securegroups", "0003_add_corporation_role_filter_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeInCorporationFilter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="The filter description that is shown to end users.",
                        max_length=500,
                    ),
                ),
                (
                    "minimum_days",
                    models.PositiveIntegerField(
                        default=30,
                        help_text="Minimum number of days a main character needs to be member of his/her current corporation.",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CorporationTitleFilter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="The filter description that is shown to end users.",
                        max_length=500,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True,
                        help_text="User must have a character with this title.",
                        max_length=100,
                    ),
                ),
                (
                    "include_alts",
                    models.BooleanField(
                        default=False,
                        help_text="When True, the filter will also include the users alt-characters.",
                    ),
                ),
                (
                    "corporations",
                    models.ManyToManyField(
                        help_text="The character with the title must be in one of these corporations.",
                        related_name="+",
                        to="eveonline.evecorporationinfo",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
