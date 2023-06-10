from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=20, verbose_name='Электронная почта')
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
    fullname = models.CharField(max_length=50, verbose_name='Полное имя')
    region = models.CharField(max_length=50, verbose_name='Область')
    city = models.CharField(max_length=50, verbose_name='Город')
    district = models.CharField(max_length=50, default='Не выбрано', choices=(
        ('leninskiy', 'Ленинский'), ('oktyabrskiy', 'Октябрьский'), ('sverdlovskiy', 'Свердловский'),
        ('pervomaiskiy', 'Первомайский')
    ), verbose_name='Район')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    email = models.EmailField(max_length=30, verbose_name='Электронная почта')
    home = models.CharField(max_length=50, verbose_name='Дом')
    apartment = models.CharField(max_length=50, default=0, verbose_name='Квартира')

    def __str__(self):
        return self.fullname


class Reading(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    reading_date = models.DateField(auto_now_add=True, verbose_name='Считывание')
    room_volume = models.FloatField(default=0, verbose_name='Объем помещения')
    heat_loss = models.FloatField(default=0, verbose_name='Теплопотеря')
    efficiency = models.FloatField(default=0, verbose_name='КПД')
    reading_value = models.FloatField(null=True, blank=True,auto_created=True, verbose_name='Значение считывания')

    def __str__(self):
        return self.property_id.fullname


class Cost(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='ID компании')
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE, verbose_name='ID считывания')
    rate = models.FloatField(verbose_name='Тариф')
    price = models.FloatField(default=0, verbose_name='Стоимость')

    def __str__(self):
        return self.property_id.fullname


class Invoice(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='ID компании')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='ID клиента')
    number = models.CharField(max_length=10, verbose_name='Номер счета')
    invoice_date = models.DateField(verbose_name='Дата счета')  # the date the invoice was issued

    def __str__(self):
        return self.number


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='Номер счета')
    name = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='Имя')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    first_payment = models.ForeignKey(Cost, on_delete=models.CASCADE, verbose_name='Первичная сумма')
    payment_amount = models.FloatField(default=0, verbose_name='Сумма платежа')
    debt = models.FloatField(default=0, verbose_name='Задолженность')



