# Generated by Django 4.0.10 on 2023-09-22 21:50

# Django
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("memberaudit", "0011_add_standings_index"),
        ("memberaudit_securegroups", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skillpointfilter",
            name="skill_point_threshold",
            field=models.PositiveBigIntegerField(
                help_text="Minimum allowable skill points."
            ),
        ),
        migrations.AlterField(
            model_name="skillsetfilter",
            name="skill_sets",
            field=models.ManyToManyField(
                help_text="Users must possess all of the skills in <strong>one</strong> of the selected skill sets.",
                to="memberaudit.skillset",
            ),
        ),
    ]
