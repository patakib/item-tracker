# Generated by Django 3.1.5 on 2021-01-15 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0005_auto_20210114_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='editing',
        ),
    ]
