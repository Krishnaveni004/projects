# Generated by Django 2.1.1 on 2018-10-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0013_auto_20181015_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshipform',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='internshipform',
            name='wrks',
        ),
        migrations.AddField(
            model_name='internshipform',
            name='internship',
            field=models.CharField(default='internship', max_length=100),
        ),
        migrations.AddField(
            model_name='internshipform',
            name='parent_contact',
            field=models.CharField(default='parent_contact', max_length=100),
        ),
        migrations.AlterField(
            model_name='internshipform',
            name='cty_w',
            field=models.CharField(default='city_for_internship', max_length=100),
        ),
    ]
