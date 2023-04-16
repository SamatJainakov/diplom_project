# Generated by Django 4.1.7 on 2023-04-02 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_vendor_vendor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='cost',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget',
            field=models.FloatField(default=0, verbose_name='Баланс'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.property', verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='price',
            field=models.FloatField(default=0, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.property', verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='usage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.usage', verbose_name='ID потребления'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.vendor', verbose_name='ID компании'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_due',
            field=models.FloatField(default=0, verbose_name='Сумма долга'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(verbose_name='Срок оплаты'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(verbose_name='Дата счета'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(max_length=50, verbose_name='Номер счета'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.property', verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.vendor', verbose_name='ID компании'),
        ),
        migrations.AlterField(
            model_name='meter',
            name='meter_location',
            field=models.CharField(max_length=50, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='meter',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.property', verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.invoice', verbose_name='ID счета'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.FloatField(default=0, verbose_name='Сумма платежа'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(auto_now=True, verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='property',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner_name',
            field=models.CharField(max_length=50, verbose_name='Имя клиента'),
        ),
        migrations.AlterField(
            model_name='property',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='property',
            name='region',
            field=models.CharField(max_length=50, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.meter', verbose_name='ID высоты'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='reading_date',
            field=models.DateField(verbose_name='Считывание'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='reading_value',
            field=models.FloatField(default=0, verbose_name='Значение считывания'),
        ),
        migrations.AlterField(
            model_name='usage',
            name='end_date',
            field=models.DateField(verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='usage',
            name='meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.meter', verbose_name='ID высоты'),
        ),
        migrations.AlterField(
            model_name='usage',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.property', verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='usage',
            name='start_date',
            field=models.DateField(verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='usage',
            name='usage_amount',
            field=models.FloatField(default=0, verbose_name='Значение потребления'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='region',
            field=models.CharField(max_length=50, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_name',
            field=models.CharField(max_length=50, verbose_name='Имя компании'),
        ),
    ]