# Generated by Django 3.0.8 on 2020-08-22 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20200822_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Barangay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Barangay'),
        ),
    ]
