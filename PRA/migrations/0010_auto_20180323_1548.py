# Generated by Django 2.0.1 on 2018-03-23 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRA', '0009_auto_20180323_1544'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewVisitor',
            new_name='Visitor',
        ),
        migrations.AlterModelTable(
            name='visitor',
            table='Visitors',
        ),
    ]
