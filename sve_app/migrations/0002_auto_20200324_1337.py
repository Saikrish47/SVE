# Generated by Django 2.2.1 on 2020-03-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sve_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
