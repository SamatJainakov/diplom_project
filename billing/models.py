from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    password = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self):
        return self.email


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50, verbose_name='Имя компании')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    city = models.CharField(max_length=50, verbose_name='Город')
    region = models.CharField(max_length=50, verbose_name='Область')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')

    def __str__(self):
        return self.vendor_name


class Property(models.Model):
    owner_name = models.CharField(max_length=50, verbose_name='Имя клиента')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    city = models.CharField(max_length=50, verbose_name='Город')
    region = models.CharField(max_length=50, verbose_name='Область')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    meter = models.CharField(max_length=50, verbose_name='Этаж')  # the location of the meter
    # (e.g. basement, first floor, etc.)

    def __str__(self):
        return self.owner_name


class Reading(models.Model):
    reading_date = models.DateField(verbose_name='Считывание')  # the date the reading was taken
    reading_value = models.IntegerField(verbose_name='Значение считывания')  # the value of the reading


class Usage(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    start_date = models.DateField(verbose_name='Начало')
    end_date = models.DateField(verbose_name='Конец')
    usage_amount = models.FloatField(default=0, verbose_name='Значение потребления')


class Cost(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='ID компании')
    usage = models.ForeignKey(Usage, on_delete=models.CASCADE, verbose_name='ID потребления')
    price = models.FloatField(default=0, verbose_name='Стоимость')


class Invoice(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='ID компании')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    invoice_number = models.CharField(max_length=50, verbose_name='Номер счета')
    invoice_date = models.DateField(verbose_name='Дата счета')  # the date the invoice was issued
    due_date = models.DateField(verbose_name='Срок оплаты')  # the date by which payment is due
    amount_due = models.FloatField(default=0, null=True, blank=True, verbose_name='Сумма долга')

    def __str__(self):
        return self.invoice_number


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='ID лицевого счета')
    payment_date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    payment_method = models.CharField(max_length=20, choices=(
        ("visa", "Visa"),
        ("mastercard", "MasterCard"),
        ("paypal", "PayPal"),
        ("elcard", "Элькарт")
    ), default='Не выбрано', verbose_name='Способ оплаты')
    payment_amount = models.FloatField(default=0, verbose_name='Сумма платежа')

