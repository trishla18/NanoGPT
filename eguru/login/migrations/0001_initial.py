# Generated by Django 4.1.7 on 2024-07-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("email", models.CharField(max_length=256)),
                ("name", models.CharField(max_length=256)),
                ("password", models.CharField(max_length=256)),
                ("created_at", models.DateTimeField()),
            ],
            options={
                "db_table": "users",
                "managed": False,
            },
        ),
    ]
