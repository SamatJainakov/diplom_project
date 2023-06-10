# Generated by Django 4.1.7 on 2023-06-10 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0021_remove_cost_usage_cost_reading_reading_property_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='rate',
            field=models.FloatField(default=1, verbose_name='Тариф'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cost',
            name='reading',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.reading', verbose_name='ID считывания'),
        ),
    ]