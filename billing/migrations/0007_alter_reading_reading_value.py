# Generated by Django 4.1.7 on 2023-05-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_payment_payment_method_alter_invoice_amount_due_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='reading_value',
            field=models.IntegerField(verbose_name='Значение считывания'),
        ),
    ]
