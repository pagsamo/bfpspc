# Generated by Django 3.0.8 on 2020-08-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20200822_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdata',
            name='nl_name_3',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
