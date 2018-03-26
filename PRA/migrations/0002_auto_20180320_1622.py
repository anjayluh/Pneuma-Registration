# Generated by Django 2.0.1 on 2018-03-20 13:22

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('PRA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Visitors',
            },
        ),
        migrations.RemoveField(
            model_name='visitors',
            name='visitor',
        ),
        migrations.DeleteModel(
            name='Visitors',
        ),
    ]