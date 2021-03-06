# Generated by Django 2.2 on 2021-01-20 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0008_auto_20210111_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_entity', to='finder.Items'),
        ),
    ]
