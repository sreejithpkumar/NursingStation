# Generated by Django 4.1.2 on 2025-03-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PanalWindow', '0006_alter_patient_info_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_info',
            name='Gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
