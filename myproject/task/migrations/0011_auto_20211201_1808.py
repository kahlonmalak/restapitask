# Generated by Django 3.2.9 on 2021-12-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20211201_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
