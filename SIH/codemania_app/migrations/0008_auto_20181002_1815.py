# Generated by Django 2.1.1 on 2018-10-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0007_contactform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='message',
        ),
        migrations.AddField(
            model_name='contactform',
            name='msg',
            field=models.CharField(default='message', max_length=200),
        ),
    ]