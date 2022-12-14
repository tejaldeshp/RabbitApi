# Generated by Django 4.1 on 2022-11-04 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CalcScenario",
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
                    "dtm_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="DTM Created"),
                ),
                (
                    "dtm_updated",
                    models.DateTimeField(auto_now=True, verbose_name="DTM Updated"),
                ),
                ("slug", models.CharField(max_length=22, unique=True)),
                ("name", models.CharField(max_length=64)),
                ("user", models.CharField(max_length=11)),
                ("is_public", models.BooleanField(default=False)),
                (
                    "price_per_run",
                    models.DecimalField(decimal_places=3, default="100", max_digits=8),
                ),
            ],
            options={
                "verbose_name": "Rabbit Calculation Scenario",
                "verbose_name_plural": "Rabbit Calculation Scenarios",
                "unique_together": {("name", "user")},
            },
        ),
        migrations.CreateModel(
            name="CalcScenarioParam",
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
                    "dtm_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="DTM Created"),
                ),
                (
                    "dtm_updated",
                    models.DateTimeField(auto_now=True, verbose_name="DTM Updated"),
                ),
                ("param", models.CharField(max_length=11)),
                (
                    "value",
                    models.CharField(
                        blank=True, default=None, max_length=32, null=True
                    ),
                ),
                (
                    "scenario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="params",
                        to="rabbit.calcscenario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Rabbit Calculation Scenario Params",
                "verbose_name_plural": "Rabbit Calculation Scenario Params",
                "unique_together": {("scenario", "param", "value")},
            },
        ),
    ]
