# Generated by Django 2.2.24 on 2021-09-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('determinations', '0010_add_determination_stream_field_forms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='determination',
            name='outcome',
            field=models.IntegerField(choices=[(0, 'Dismissed'), (1, 'More information requested'), (2, 'Approved')], verbose_name='Determination'),
        ),
    ]
