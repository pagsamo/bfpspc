# Generated by Django 3.0.8 on 2020-12-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_incident_occupancytype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ('-DateCalled', 'Barangay')},
        ),
        migrations.AddField(
            model_name='incident',
            name='DateCalled',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='TimeCalled',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='incident',
            unique_together={('DateCalled', 'OwnerName')},
        ),
        migrations.RemoveField(
            model_name='incident',
            name='DateTime',
        ),
    ]
