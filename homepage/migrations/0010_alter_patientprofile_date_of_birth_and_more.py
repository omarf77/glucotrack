# Generated by Django 5.2.3 on 2025-07-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_alter_patientprofile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='finger_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
