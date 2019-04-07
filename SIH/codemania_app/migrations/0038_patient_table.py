# Generated by Django 2.1.7 on 2019-02-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0037_auto_20190227_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(default='pid', max_length=6)),
                ('did', models.CharField(default='did', max_length=100)),
                ('diseasename', models.CharField(default='fever', max_length=200)),
                ('date', models.DateTimeField(max_length=100)),
                ('linkreport', models.CharField(max_length=200)),
            ],
        ),
    ]