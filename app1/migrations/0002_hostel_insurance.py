# Generated by Django 4.2.2 on 2023-10-04 00:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []
    

    operations = [
        migrations.CreateModel(
            name="Hostel",
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
        migrations.CreateModel(
            name="Insurance",
            fields=[
                (
                    "client_id",
                    models.AutoField(default=1, primary_key=True, serialize=False),
                ),
                ("pet", models.CharField(max_length=15, null=True)),
                ("owner_name", models.CharField(max_length=15, null=True)),
                ("Insurance_name", models.CharField(max_length=50, null=True)),
                ("start_date", models.DateField(null=True)),
                (
                    "contactnumber",
                    models.CharField(
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{10}$", "Enter a 10-digit number."
                            )
                        ],
                    ),
                ),
            ],
        ),
    ]
