# Generated by Django 4.2.3 on 2023-07-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_student_gpa_alter_student_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('CS', 'CS'), ('IS', 'IS'), ('BIO', 'BIO'), ('None', 'None')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('3', '3'), ('2', '2'), ('4', '4'), ('1', '1')], max_length=1, verbose_name='level'),
        ),
    ]
