# Generated by Django 3.1.3 on 2020-11-15 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfl_next_gen_stats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passingstats',
            old_name='gsis_id',
            new_name='gsis',
        ),
    ]
