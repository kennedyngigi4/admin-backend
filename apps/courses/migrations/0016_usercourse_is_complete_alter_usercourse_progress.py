# Generated by Django 4.2 on 2025-02-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_usercourse_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='progress',
            field=models.CharField(choices=[('progress', 'progress'), ('completed', 'completed')], default='progress', max_length=20, null=True),
        ),
    ]
