# Generated by Django 4.2 on 2025-02-16 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_usercourse_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercourse',
            name='access_type',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='certificate_url',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='completed_at',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='course',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='purchase_id',
        ),
    ]
