# Generated by Django 5.2.3 on 2025-07-01 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_medicalstaffprofile'),
        ('patient_blood', '0002_alter_addentry_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addentry',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homepage.patientprofile'),
            preserve_default=False,
        ),
    ]
