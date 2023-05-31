# Generated by Django 4.1.7 on 2023-05-05 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_remove_meter_property_id_remove_reading_meter_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='meter_location',
            new_name='meter',
        ),
        migrations.AlterField(
            model_name='payment',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.invoice', verbose_name='ID тарифа'),
        ),
    ]