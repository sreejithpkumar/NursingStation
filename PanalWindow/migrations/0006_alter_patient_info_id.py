# Generated by Django 4.1.2 on 2025-03-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PanalWindow', '0005_alter_patient_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
