# Generated by Django 2.2.7 on 2020-08-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('source_code', models.TextField(blank=True, null=True)),
                ('language_choices', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
