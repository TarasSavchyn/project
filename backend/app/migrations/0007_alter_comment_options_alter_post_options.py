# Generated by Django 4.1 on 2024-03-04 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_comment_parent_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
    ]