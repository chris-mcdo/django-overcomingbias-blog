# Generated by Django 4.0.3 on 2022-07-10 23:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("obapi", "0004_essaycontentitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="sequence",
            name="create_timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text="When the sequence was created.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sequence",
            name="update_timestamp",
            field=models.DateTimeField(
                auto_now=True,
                help_text="When the sequence was last updated.",
                verbose_name="update date",
            ),
        ),
    ]
