# Generated by Django 4.1 on 2023-07-16 07:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("client_name", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "contactnumber",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{10}$", "Enter a 10-digit number."
                            )
                        ],
                    ),
                ),
                ("message", models.TextField()),
            ],
        ),
    ]
