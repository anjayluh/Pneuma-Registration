# Generated by Django 2.0.1 on 2018-03-23 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRA', '0008_auto_20180323_1542'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visitor',
            new_name='NewVisitor',
        ),
        migrations.AlterModelTable(
            name='newvisitor',
            table='New Visitor',
        ),
    ]
