# Generated by Django 4.2 on 2023-04-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='data',
            field=models.JSONField(),
        ),
    ]
