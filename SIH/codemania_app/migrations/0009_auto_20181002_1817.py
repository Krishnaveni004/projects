# Generated by Django 2.1.1 on 2018-10-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0008_auto_20181002_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='msg',
            field=models.TextField(default='message', max_length=200),
        ),
    ]