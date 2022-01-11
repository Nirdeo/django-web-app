# Generated by Django 4.0.1 on 2022-01-11 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_band_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
                ('type', models.CharField(choices=[('R', 'Records'), ('C', 'Clothing'), ('P', 'Posters'), ('M', 'Misc')], max_length=5)),
            ],
        ),
    ]