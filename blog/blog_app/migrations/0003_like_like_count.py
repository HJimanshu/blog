# Generated by Django 5.1.1 on 2024-09-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_rename_content_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
