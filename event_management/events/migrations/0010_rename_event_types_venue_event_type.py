# Generated by Django 4.1.5 on 2023-02-01 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_venue_event_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='event_types',
            new_name='event_type',
        ),
    ]
