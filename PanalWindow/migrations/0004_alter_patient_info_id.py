# Generated by Django 4.1.2 on 2025-03-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PanalWindow', '0003_alter_patient_info_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
