# Generated by Django 5.1 on 2024-09-06 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0023_alter_segment_date_of_r_awn1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segment',
            old_name='question_received_date',
            new_name='questionnaire_received_date',
        ),
    ]
