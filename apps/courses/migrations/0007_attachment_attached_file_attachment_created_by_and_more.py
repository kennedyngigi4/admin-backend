# Generated by Django 4.2 on 2025-02-14 09:22

import apps.courses.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_chapter_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='attached_file',
            field=models.FileField(null=True, upload_to=apps.courses.models.AttachmentPath),
        ),
        migrations.AddField(
            model_name='attachment',
            name='created_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.chapter'),
        ),
    ]
