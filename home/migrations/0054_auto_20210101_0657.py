# Generated by Django 3.0.8 on 2020-12-31 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_delete_spotinvestigation'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='incidentresponse',
            unique_together={('Incident', 'Engine')},
        ),
    ]
