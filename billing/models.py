from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    password = models.CharField(max_length=50, verbose_name='Пароль')


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50, verbose_name='Имя компании')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    city = models.CharField(max_length=50, verbose_name='Город')
    region = models.CharField(max_length=50, verbose_name='Область')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')


class Property(models.Model):
    owner_name = models.CharField(max_length=50, verbose_name='Имя клиента')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    city = models.CharField(max_length=50, verbose_name='Город')
    region = models.CharField(max_length=50, verbose_name='Область')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')


class Meter(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    meter_location = models.CharField(max_length=50, verbose_name='Этаж')  # the location of the meter
    # (e.g. basement, first floor, etc.)


class Reading(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, verbose_name='ID высоты')
    reading_date = models.DateField(verbose_name='Считывание')  # the date the reading was taken
    reading_value = models.FloatField(default=0, verbose_name='Значение считывания')  # the value of the reading


class Usage(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, verbose_name='ID высоты')
    start_date = models.DateField(verbose_name='Начало')
    end_date = models.DateField(verbose_name='Конец')
    usage_amount = models.FloatField(default=0, verbose_name='Значение потребления')


class Cost(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='ID компании')
    usage = models.ForeignKey(Usage, on_delete=models.CASCADE, verbose_name='ID потребления')
    price = models.FloatField(default=0, verbose_name='Стоимость')


class Budget(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    budget = models.FloatField(default=0, verbose_name='Баланс')


class Invoice(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='ID компании')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    invoice_number = models.CharField(max_length=50, verbose_name='Номер счета')
    invoice_date = models.DateField(verbose_name='Дата счета')  # the date the invoice was issued
    due_date = models.DateField(verbose_name='Срок оплаты')  # the date by which payment is due
    amount_due = models.FloatField(default=0, verbose_name='Сумма долга')  # the total amount due on the invoice


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='ID счета')
    payment_date = models.DateField(auto_now=True, verbose_name='Дата оплаты')  # the date the payment was made
    payment_amount = models.FloatField(default=0, verbose_name='Сумма платежа')  # the amount of the payment
