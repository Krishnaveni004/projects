# Generated by Django 2.1.4 on 2019-01-20 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0027_auto_20190120_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField(default=0)),
                ('course_name', models.CharField(default='course', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.ForeignKey(default='course', on_delete=django.db.models.deletion.CASCADE, to='codemania_app.CourseDesc'),
        ),
    ]
