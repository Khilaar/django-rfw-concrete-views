# Generated by Django 5.0 on 2023-12-26 17:09

import registration_profile.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration_profile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registrationprofile",
            name="code",
            field=models.CharField(
                default=registration_profile.models.code_generator, max_length=5
            ),
        ),
    ]
