# Generated by Django 2.1.4 on 2019-01-20 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codemania_app', '0026_companies_companyform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='companies',
            name='course',
            field=models.CharField(default='course', max_length=50),
        ),
        migrations.AddField(
            model_name='companies',
            name='skills_required',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='codemania_app.Course'),
        ),
    ]