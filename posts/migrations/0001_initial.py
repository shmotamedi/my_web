# Generated by Django 4.1.12 on 2023-12-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50)),
                ("text", models.TextField()),
                ("is_enable", models.BooleanField(default=False)),
                ("created_time", models.DateTimeField()),
                ("updated_time", models.DateTimeField()),
            ],
        ),
    ]
