# Generated by Django 3.0.4 on 2020-03-30 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0029_a_b_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='b',
            name='a',
        ),
        migrations.RemoveField(
            model_name='c',
            name='a',
        ),
        migrations.RemoveField(
            model_name='diseasecondition',
            name='conditions',
        ),
        migrations.RemoveField(
            model_name='diseasecondition',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='diseasename',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='diseasesymptom',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='diseasesymptom',
            name='symptoms',
        ),
        migrations.RemoveField(
            model_name='symptomname',
            name='symptom',
        ),
        migrations.DeleteModel(
            name='A',
        ),
        migrations.DeleteModel(
            name='B',
        ),
        migrations.DeleteModel(
            name='C',
        ),
        migrations.DeleteModel(
            name='Condition',
        ),
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.DeleteModel(
            name='DiseaseCondition',
        ),
        migrations.DeleteModel(
            name='DiseaseName',
        ),
        migrations.DeleteModel(
            name='DiseaseSymptom',
        ),
        migrations.DeleteModel(
            name='Symptom',
        ),
        migrations.DeleteModel(
            name='SymptomName',
        ),
    ]
