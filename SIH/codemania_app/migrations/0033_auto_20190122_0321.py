# Generated by Django 2.1.4 on 2019-01-22 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0032_companydetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Companies',
            new_name='Company',
        ),
        migrations.RenameModel(
            old_name='CompanyDetails',
            new_name='CompanyDetail',
        ),
    ]