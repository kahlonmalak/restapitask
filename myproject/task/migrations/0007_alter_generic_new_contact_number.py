# Generated by Django 3.2.9 on 2021-12-01 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_generic_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generic_new',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]
