# Generated by Django 4.1 on 2022-08-13 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_city_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
