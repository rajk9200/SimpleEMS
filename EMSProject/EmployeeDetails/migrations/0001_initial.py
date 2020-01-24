# Generated by Django 2.2.1 on 2020-01-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pan_number', models.CharField(max_length=10, unique=True)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=8)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
    ]
