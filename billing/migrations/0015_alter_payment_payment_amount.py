# Generated by Django 4.1.7 on 2023-06-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0014_alter_payment_invoice_alter_payment_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.FloatField(default=0, verbose_name='Сумма платежа'),
        ),
    ]
