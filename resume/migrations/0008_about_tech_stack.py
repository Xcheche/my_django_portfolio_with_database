# Generated by Django 5.0.6 on 2024-07-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0007_certificates"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="tech_stack",
            field=models.ImageField(default="Okay", upload_to="images/tech_stack"),
        ),
    ]
