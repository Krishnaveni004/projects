# Generated by Django 2.1.4 on 2019-01-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0024_studentdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='course',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='program_name',
            field=models.CharField(max_length=50),
        ),
    ]
