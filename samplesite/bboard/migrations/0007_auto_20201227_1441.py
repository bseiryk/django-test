# Generated by Django 2.2 on 2020-12-27 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_auto_20201227_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinValueValidator('4')]),
        ),
    ]
