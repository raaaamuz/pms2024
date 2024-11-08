# Generated by Django 5.1 on 2024-08-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0005_segment_segment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segment',
            name='item',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='segment',
            name='segment_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='segment',
            name='segment_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='segment',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]