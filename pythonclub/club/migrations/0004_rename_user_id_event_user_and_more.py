# Generated by Django 4.0.3 on 2022-04-26 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_rename_meeting_date_meeting_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='meetingminutes',
            old_name='meeting_id',
            new_name='meeting',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='user_id',
            new_name='user',
        ),
    ]