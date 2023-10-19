# Generated by Django 4.0.10 on 2023-10-12 18:12

# Django
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("memberaudit", "0013_add_corporation_titles"),
        ("eveonline", "0017_alliance_and_corp_names_are_not_unique"),
        (
            "memberaudit_securegroups",
            "0002_alter_skillpointfilter_skill_point_threshold_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="skillsetfilter",
            name="character_type",
            field=models.CharField(
                blank=True,
                choices=[("AN", "Any"), ("MO", "Mains only"), ("AO", "Alts only")],
                default="AN",
                help_text="Specify the type of character that needs to have the skill set.",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="skillsetfilter",
            name="skill_sets",
            field=models.ManyToManyField(
                help_text="Users must have a character who possess all of the skills in <strong>one</strong> of the selected skill sets.",
                to="memberaudit.skillset",
            ),
        ),
        migrations.CreateModel(
            name="CorporationRoleFilter",
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
                    "role",
                    models.CharField(
                        choices=[
                            ("AT1", "account take 1"),
                            ("AT2", "account take 2"),
                            ("AT3", "account take 3"),
                            ("AT4", "account take 4"),
                            ("AT5", "account take 5"),
                            ("AT6", "account take 6"),
                            ("AT7", "account take 7"),
                            ("ACT", "accountant"),
                            ("AUD", "auditor"),
                            ("COM", "communications officer"),
                            ("CEQ", "config equipment"),
                            ("CSE", "config starbase equipment"),
                            ("CT1", "container take 1"),
                            ("CT2", "container take 2"),
                            ("CT3", "container take 3"),
                            ("CT4", "container take 4"),
                            ("CT5", "container take 5"),
                            ("CT6", "container take 6"),
                            ("CT7", "container take 7"),
                            ("CMG", "contract manager"),
                            ("DPL", "diplomat"),
                            ("DRT", "director"),
                            ("FCM", "factory manager"),
                            ("FTM", "fitting manager"),
                            ("HQ1", "hangar query 1"),
                            ("HQ2", "hangar query 2"),
                            ("HQ3", "hangar query 3"),
                            ("HQ4", "hangar query 4"),
                            ("HQ5", "hangar query 5"),
                            ("HQ6", "hangar query 6"),
                            ("HQ7", "hangar query 7"),
                            ("HT1", "hangar take 1"),
                            ("HT2", "hangar take 2"),
                            ("HT3", "hangar take 3"),
                            ("HT4", "hangar take 4"),
                            ("HT5", "hangar take 5"),
                            ("HT6", "hangar take 6"),
                            ("HT7", "hangar take 7"),
                            ("JAC", "junior accountant"),
                            ("PSM", "personnel manager"),
                            ("RFF", "rent factory facility"),
                            ("RFC", "rent office"),
                            ("RRF", "rent research facility"),
                            ("SCO", "security officer"),
                            ("SPM", "skill plan manager"),
                            ("SDO", "starbase defense operator"),
                            ("SFT", "starbase fuel technician"),
                            ("STM", "station manager"),
                            ("TRD", "trader"),
                        ],
                        db_index=True,
                        help_text="User must have a character with this role.",
                        max_length=3,
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
                        help_text="The character with the role must be in one of these corporations.",
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
