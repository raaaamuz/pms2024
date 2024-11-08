# Generated by Django 5.0.2 on 2024-03-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_norms_acidityofoil_alter_norms_aftertaste_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='norms',
            name='blindbranded',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='norms',
            name='clientname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='norms',
            name='countrycode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='exactage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='jobno',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='norms',
            name='nationality',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='placeofinterview',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='projectname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='norms',
            name='respondentid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='studydesign',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='studytype',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='supercategory',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='norms',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]