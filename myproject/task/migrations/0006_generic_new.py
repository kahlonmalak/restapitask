# Generated by Django 3.2.9 on 2021-12-01 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20211130_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generic_new',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField()),
                ('contact_number', models.IntegerField(max_length=10)),
            ],
        ),
    ]
