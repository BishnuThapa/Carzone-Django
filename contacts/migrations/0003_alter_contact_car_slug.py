# Generated by Django 4.1 on 2022-08-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_remove_contact_car_id_contact_car_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='car_slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]