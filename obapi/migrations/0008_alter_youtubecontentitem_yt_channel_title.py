# Generated by Django 4.0.3 on 2022-11-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("obapi", "0007_rename_text_html_textcontentitem_text_html_tmp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="youtubecontentitem",
            name="yt_channel_title",
            field=models.CharField(
                help_text="Channel title.", max_length=100, verbose_name="channel title"
            ),
        ),
    ]
