# Generated by Django 3.2.13 on 2022-05-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0097_applicationbaseexternalreviewform_labbaseexternalreviewform_roundbaseexternalreviewform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationsubmission',
            name='submit_time',
            field=models.DateTimeField(verbose_name='submit time'),
        ),
    ]
