# Generated by Django 4.1 on 2024-03-04 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_post_comments"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SubComment",
        ),
    ]