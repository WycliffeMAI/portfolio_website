# Generated by Django 4.2.5 on 2024-04-04 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("site_settings", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="socialmediasettings", old_name="skype", new_name="zoom",
        ),
    ]
