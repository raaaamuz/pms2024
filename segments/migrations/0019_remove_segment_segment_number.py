# Generated by Django 5.1 on 2024-09-05 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0018_segment_segment_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segment',
            name='segment_number',
        ),
    ]
