# Generated by Django 2.2.7 on 2020-08-08 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.Post'),
        ),
    ]
