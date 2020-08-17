# Generated by Django 2.2.7 on 2020-08-15 13:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moderator', '0002_course_section'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0002_input_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('course', models.ManyToManyField(to='Moderator.Course')),
                ('section', models.ManyToManyField(to='Moderator.Section')),
                ('student', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('course', models.ManyToManyField(to='Moderator.Course')),
                ('section', models.ManyToManyField(to='Moderator.Section')),
                ('student', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
