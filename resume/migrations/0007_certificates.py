# Generated by Django 5.0.6 on 2024-07-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0006_alter_experience_options_remove_experience_company_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Certificates",
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
                ("title", models.CharField(max_length=100)),
                ("certificate_id", models.CharField(blank=True, max_length=25)),
            ],
            options={
                "verbose_name_plural": "Certificates",
            },
        ),
    ]
