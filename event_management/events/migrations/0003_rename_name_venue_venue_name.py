# Generated by Django 4.1.3 on 2023-01-23 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventuser_event_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='name',
            new_name='venue_name',
        ),
    ]
