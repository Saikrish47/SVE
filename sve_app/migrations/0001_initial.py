# Generated by Django 2.2.1 on 2020-03-24 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('saled', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('time', models.DateField(blank=True, null=True)),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sve_app.Prime')),
            ],
        ),
    ]
