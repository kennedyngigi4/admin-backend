# Generated by Django 4.2 on 2025-02-16 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_usercourse_access_type_usercourse_certificate_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
