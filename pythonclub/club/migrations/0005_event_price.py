# Generated by Django 4.0.3 on 2022-06-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_rename_user_id_event_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]