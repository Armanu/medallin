# Generated by Django 3.0.4 on 2020-03-30 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0032_auto_20200330_1858'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together={('concept', 'language')},
        ),
    ]
