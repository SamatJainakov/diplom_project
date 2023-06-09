# Generated by Django 4.1.7 on 2023-05-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_remove_cost_end_date_remove_cost_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meter',
            name='property_id',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='meter',
        ),
        migrations.RemoveField(
            model_name='usage',
            name='meter',
        ),
        migrations.AddField(
            model_name='property',
            name='meter_location',
            field=models.CharField(default=1, max_length=50, verbose_name='Этаж'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.DeleteModel(
            name='Meter',
        ),
    ]
