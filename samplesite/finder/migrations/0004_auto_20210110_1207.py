# Generated by Django 2.2 on 2021-01-10 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_auto_20210110_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finder.Items'),
        ),
    ]
