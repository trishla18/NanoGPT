# Generated by Django 4.1.7 on 2024-07-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CourseMaterial",
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
                ("topic_id", models.CharField(max_length=256)),
                ("file_location", models.TextField()),
            ],
            options={
                "db_table": "course_material",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Faculty",
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
                ("name", models.CharField(max_length=256)),
                ("email", models.CharField(max_length=256)),
                ("designation", models.CharField(max_length=256)),
                ("about", models.TextField()),
                ("topic_id", models.CharField(max_length=256)),
            ],
            options={
                "db_table": "faculty",
                "managed": False,
            },
        ),
    ]