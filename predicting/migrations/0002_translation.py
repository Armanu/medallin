# Generated by Django 3.0.4 on 2020-03-23 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(choices=[('en-us', 'English (United States)'), ('fa-ir', 'فارسی (ایران)')], max_length=5, verbose_name='Locale')),
                ('string', models.CharField(max_length=128, verbose_name='String')),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predicting.Concept', verbose_name='Concept')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
    ]
