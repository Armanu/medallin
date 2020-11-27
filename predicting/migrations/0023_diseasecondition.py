# Generated by Django 3.0.4 on 2020-03-24 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0022_auto_20200324_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.ManyToManyField(to='predicting.Condition')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting.Disease')),
            ],
        ),
    ]
