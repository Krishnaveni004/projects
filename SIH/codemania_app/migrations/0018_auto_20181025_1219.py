# Generated by Django 2.1.1 on 2018-10-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0017_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshipform',
            name='cty_i',
        ),
        migrations.AddField(
            model_name='internshipform',
            name='review',
            field=models.CharField(default='review', max_length=100),
        ),
    ]
