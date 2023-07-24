# Generated by Django 4.2.3 on 2023-07-24 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_remove_grade_user_grade_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('BIO', 'BIO'), ('CS', 'CS'), ('IS', 'IS'), ('None', 'None')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('3', '3'), ('4', '4'), ('2', '2'), ('1', '1')], max_length=1, verbose_name='level'),
        ),
    ]
