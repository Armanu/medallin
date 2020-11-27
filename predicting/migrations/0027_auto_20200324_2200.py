# Generated by Django 3.0.4 on 2020-03-24 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0026_auto_20200324_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(choices=[('en-us', 'English (United States)'), ('fa-ir', 'فارسی (ایران)')], max_length=5, verbose_name='زبان')),
                ('string', models.CharField(max_length=256, verbose_name='رشته')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting.Disease')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SymptomName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(choices=[('en-us', 'English (United States)'), ('fa-ir', 'فارسی (ایران)')], max_length=5, verbose_name='زبان')),
                ('string', models.CharField(max_length=256, verbose_name='رشته')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting.Symptom')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Translation',
        ),
        migrations.AlterModelOptions(
            name='diseasesymptom',
            options={'verbose_name': 'علائم بیماری', 'verbose_name_plural': 'علائم بیماری'},
        ),
        migrations.AlterField(
            model_name='condition',
            name='expression',
            field=models.TextField(help_text='متن وارد\u200cشده می\u200cبایست یک Expression معتبر پایتونی باشد. متغیر\u200cها می\u200cبایست درون { } قرار گیرند.', verbose_name='عبارت'),
        ),
        migrations.AlterField(
            model_name='diseasesymptom',
            name='symptoms',
            field=models.ManyToManyField(to='predicting.Symptom', verbose_name='علامت\u200cهای مرتبط'),
        ),
    ]
