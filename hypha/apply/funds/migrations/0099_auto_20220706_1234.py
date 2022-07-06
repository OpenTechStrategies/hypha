# Generated by Django 3.2.13 on 2022-07-06 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0052_projectapprovalform'),
        ('funds', '0098_alter_applicationsubmission_submit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationbase',
            name='approval_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funds', to='application_projects.projectapprovalform'),
        ),
        migrations.AddField(
            model_name='labbase',
            name='approval_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='labs', to='application_projects.projectapprovalform'),
        ),
    ]
