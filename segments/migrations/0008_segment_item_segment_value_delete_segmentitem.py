# Generated by Django 5.1 on 2024-08-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0007_remove_segment_item_remove_segment_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='item',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='segment',
            name='value',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='SegmentItem',
        ),
    ]