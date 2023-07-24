# Generated by Django 4.2.3 on 2023-07-24 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_remove_student_grade_alter_student_department_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='attendance',
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('CS', 'CS'), ('IS', 'IS'), ('None', 'None'), ('BIO', 'BIO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('4', '4'), ('3', '3'), ('1', '1'), ('2', '2')], max_length=1, verbose_name='level'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=20)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.instructor')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
    ]
