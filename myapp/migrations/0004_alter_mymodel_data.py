# Generated by Django 4.2 on 2023-04-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_mymodel_data_alter_mymodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
