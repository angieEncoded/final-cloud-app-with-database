# Generated by Django 4.0.5 on 2022-07-21 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_alter_choice_id_alter_course_id_alter_enrollment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='associated_lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_lesson', to='onlinecourse.lesson'),
        ),
    ]
