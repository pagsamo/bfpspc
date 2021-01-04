# Generated by Django 3.0.8 on 2021-01-02 10:18

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_incident_disposition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Details',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Observations',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Problems',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
