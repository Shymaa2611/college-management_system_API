# Generated by Django 4.2.3 on 2023-07-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_mobile_user_alter_department_department_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_mobile',
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('None', 'None'), ('CS', 'CS'), ('IS', 'IS'), ('BIO', 'BIO')], max_length=10, verbose_name='department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('3', '3'), ('2', '2'), ('4', '4'), ('1', '1')], max_length=1, verbose_name='level'),
        ),
    ]
