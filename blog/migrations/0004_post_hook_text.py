# Generated by Django 4.1.6 on 2023-03-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="hook_text",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]