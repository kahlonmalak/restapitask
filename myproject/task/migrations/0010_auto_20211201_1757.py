# Generated by Django 3.2.9 on 2021-12-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_rename_new_view_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
