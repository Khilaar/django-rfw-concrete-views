# Generated by Django 5.0 on 2023-12-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cookbook",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("recipes", models.ManyToManyField(to="recipe.recipe")),
            ],
        ),
    ]
