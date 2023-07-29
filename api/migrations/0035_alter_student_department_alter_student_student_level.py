# Generated by Django 4.2.3 on 2023-07-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_student_department_alter_student_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('BIO', 'BIO'), ('IS', 'IS'), ('None', 'None'), ('CS', 'CS')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('1', '1'), ('3', '3')], max_length=1, verbose_name='level'),
        ),
    ]