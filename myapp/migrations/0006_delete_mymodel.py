# Generated by Django 4.2 on 2023-04-19 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_mymodel_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
