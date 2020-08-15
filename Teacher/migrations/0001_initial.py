# Generated by Django 2.2.7 on 2020-08-08 05:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Input_file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Output_file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Problem_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Problem_Rank', models.CharField(blank=True, max_length=255, null=True)),
                ('Memory_Size', models.FloatField(blank=True, default=None, null=True)),
                ('Time_Limit', models.FloatField(blank=True, default=None, null=True)),
                ('Output_Limit', models.FloatField(blank=True, default=None, null=True)),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('Testcase_Number', models.IntegerField(blank=True, default=None, null=True)),
                ('Testcase_Linenumber', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
                ('report', models.TextField(blank=True, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Input')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(blank=True, max_length=255, null=True)),
                ('examainer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('exam_starting_time', models.DateTimeField()),
                ('exam_ending_time', models.DateTimeField()),
                ('problem', models.ManyToManyField(to='Teacher.Post')),
            ],
        ),
    ]
