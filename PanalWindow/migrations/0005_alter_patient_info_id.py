# Generated by Django 4.1.2 on 2025-03-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PanalWindow', '0004_alter_patient_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
