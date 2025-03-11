# Generated by Django 5.1.4 on 2025-01-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageURL",
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
                    "online_url",
                    models.URLField(max_length=500, verbose_name="Online URL"),
                ),
                (
                    "offline_url",
                    models.CharField(
                        max_length=500, verbose_name="Offline URL (Static)"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Description",
                    ),
                ),
            ],
        ),
    ]
