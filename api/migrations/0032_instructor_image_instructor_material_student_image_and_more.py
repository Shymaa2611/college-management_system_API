# Generated by Django 4.2.3 on 2023-07-24 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_grade_student_alter_student_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='instructor/photo/'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='material',
            field=models.FileField(blank=True, null=True, upload_to='material/'),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student/photo/'),
        ),
        migrations.AddField(
            model_name='student',
            name='sheet',
            field=models.FileField(blank=True, null=True, upload_to='tasks/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('None', 'None'), ('CS', 'CS'), ('BIO', 'BIO'), ('IS', 'IS')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_level',
            field=models.CharField(choices=[('4', '4'), ('1', '1'), ('3', '3'), ('2', '2')], max_length=1, verbose_name='level'),
        ),
    ]
