# Generated by Django 3.0.4 on 2020-03-31 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0038_auto_20200331_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='factor',
            field=models.FloatField(),
        ),
    ]
