# Generated by Django 3.2 on 2021-05-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0036_auto_20210509_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='classType',
            field=models.CharField(choices=[('Economy', 'Economy'), ('Premium economy', 'Premium economy'), ('Business', 'Business'), ('First class', 'First class')], max_length=64),
        ),
    ]
