# Generated by Django 5.2.3 on 2025-07-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_blood', '0004_alter_addentry_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='addentry',
            name='seen_by_doctor',
            field=models.BooleanField(default=False),
        ),
    ]
