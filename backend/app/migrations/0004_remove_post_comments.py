# Generated by Django 4.1 on 2024-03-04 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_post_comments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="comments",
        ),
    ]
