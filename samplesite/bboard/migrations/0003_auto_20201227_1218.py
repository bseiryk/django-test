# Generated by Django 2.2 on 2020-12-27 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20201224_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='rubric',
            options={},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('salary_min', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_hired', models.BooleanField(default=False)),
                ('birth_date', models.DateTimeField(null=True)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_query_name='entries', to='bboard.Education')),
                ('expertise', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bboard.Expertise')),
                ('technologies', models.ManyToManyField(to='bboard.Technology')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
