# Generated by Django 5.0.2 on 2024-04-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='filters',
        ),
        migrations.AddField(
            model_name='filter',
            name='filter_data',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
