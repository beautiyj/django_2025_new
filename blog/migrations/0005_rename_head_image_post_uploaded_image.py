# Generated by Django 5.2.4 on 2025-08-01 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_head_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="head_image",
            new_name="uploaded_image",
        ),
    ]
