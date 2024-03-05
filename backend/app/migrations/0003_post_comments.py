# Generated by Django 4.1 on 2024-03-04 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_post_comments_remove_subcomment_post_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="comments",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_post",
                to="app.comment",
            ),
        ),
    ]
