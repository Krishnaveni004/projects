# Generated by Django 2.1.4 on 2019-01-22 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0033_auto_20190122_0321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_id',
            new_name='course_name',
        ),
    ]