# Generated by Django 3.0.8 on 2021-01-03 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0060_auto_20210103_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Cause',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
