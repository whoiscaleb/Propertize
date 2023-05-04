# Generated by Django 4.2 on 2023-05-04 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_showing_time_alter_property_type_alter_showing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='date',
            field=models.DateField(default=datetime.date(2023, 5, 4), verbose_name='showing date'),
        ),
        migrations.AlterField(
            model_name='showing',
            name='time',
            field=models.TimeField(default=datetime.time(12, 0), verbose_name='showing time'),
        ),
    ]