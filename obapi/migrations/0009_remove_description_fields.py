# Generated by Django 4.0.3 on 2022-11-27 13:07

from django.db import migrations, models


def copy_description_html_to_new_field(apps, schema_editor):
    app_name = "obapi"

    # which fields should be copied to which, on which models?
    model_names_and_maps = {
        "SpotifyContentItem": [("description_html", "description_html_tmp")],
        "YoutubeContentItem": [("description_html", "description_html_tmp")],
    }

    # Update and save items one by one
    # This is a bit slow, but it only needs to run once, so not a big deal
    for model_name, field_maps in model_names_and_maps.items():
        ContentModel = apps.get_model(app_name, model_name)
        for item in ContentModel.objects.all():
            for source_name, target_name in field_maps:
                setattr(item, target_name, getattr(item, source_name))
            item.save()


class Migration(migrations.Migration):

    dependencies = [
        ("obapi", "0008_alter_youtubecontentitem_yt_channel_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="spotifycontentitem",
            name="description_html_tmp",
            field=models.TextField(
                blank=True, help_text="HTML description of episode.", max_length=5000
            ),
        ),
        migrations.AddField(
            model_name="youtubecontentitem",
            name="description_html_tmp",
            field=models.TextField(
                blank=True, help_text="HTML description of video.", max_length=5000
            ),
        ),
        migrations.RunPython(
            copy_description_html_to_new_field, migrations.RunPython.noop
        ),
        migrations.RemoveField(
            model_name="contentitem",
            name="description_html",
        ),
        migrations.RemoveField(
            model_name="essaycontentitem",
            name="text_plain",
        ),
        migrations.RemoveField(
            model_name="obcontentitem",
            name="text_plain",
        ),
        migrations.RemoveField(
            model_name="spotifycontentitem",
            name="sp_description",
        ),
        migrations.RemoveField(
            model_name="youtubecontentitem",
            name="yt_description",
        ),
        migrations.RenameField(
            model_name="spotifycontentitem",
            old_name="description_html_tmp",
            new_name="description_html",
        ),
        migrations.RenameField(
            model_name="youtubecontentitem",
            old_name="description_html_tmp",
            new_name="description_html",
        ),
    ]
