# Generated by Django 3.1.5 on 2021-01-14 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0004_auto_20201103_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='action_started',
        ),
        migrations.RemoveField(
            model_name='task',
            name='business_segment',
        ),
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='task',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='task',
            name='email_subject',
        ),
        migrations.RemoveField(
            model_name='task',
            name='output_number',
        ),
        migrations.RemoveField(
            model_name='task',
            name='pass_or_fail',
        ),
        migrations.RemoveField(
            model_name='task',
            name='supplier_email',
        ),
        migrations.RemoveField(
            model_name='task',
            name='supplier_number',
        ),
        migrations.RemoveField(
            model_name='task',
            name='system',
        ),
        migrations.RemoveField(
            model_name='task',
            name='ticket_number',
        ),
    ]