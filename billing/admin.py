from django.contrib import admin
from django.db.models import Sum
from datetime import date

from .models import Vendor, Property, Payment, Reading, Cost, Invoice, User


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'address', 'city', 'region', 'phone_number', 'email']
    search_fields = ['vendor_name', 'address']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'address', 'city', 'district', 'region', 'phone_number', 'email']
    search_fields = ['district', ]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    date_hierarchy = "payment_date"
    list_display = ['get_row_number', 'invoice', 'name', 'payment_date',
                    'first_payment', 'payment_amount', 'debt', 'total_payment']
    fields = ['invoice', 'name', 'first_payment', 'payment_date', 'payment_amount']
    search_fields = ['name', ]
    list_filter = ['name__district', ]
    list_display_links = ['name', ]

    def debt_amount(self, request, obj, form, change):
        obj.debt = obj.first_payment.price - obj.payment_amount
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        obj.debt = obj.first_payment.price - obj.payment_amount
        obj.save()

    def get_row_number(self, obj):
        queryset = Payment.objects.all().order_by('-id')
        row_number = list(queryset).index(obj) + 1
        return row_number
    get_row_number.short_description = '№'

    def total_payment(self, obj):
        today = date.today()
        quarter_start = (today.month - 1) // 3 * 3 + 1
        quarter_end = quarter_start + 2

        sum_payment = Payment.objects.filter().aggregate(total=Sum('payment_amount'))
        return sum_payment['total']

    total_payment.short_description = 'Общая сумма'


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    date_hierarchy = "reading_date"
    list_display = ['property_id', 'reading_date', 'room_volume', 'heat_loss', 'efficiency', 'reading_value']
    fields = ['property_id', 'room_volume', 'heat_loss', 'efficiency']
    search_fields = ['reading_value']

    def reading(self, request, obj, form, change):
        obj.reading_value = obj.room_volume * obj.heat_loss / obj.efficiency
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        obj.reading_value = obj.room_volume * obj.heat_loss / obj.efficiency
        obj.save()


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'vendor', 'reading', 'rate', 'price']
    fields = ['property_id', 'vendor', 'reading', 'rate']
    search_fields = ['property_id', 'price']

    def save_model(self, request, obj, form, change):
        obj.price = obj.reading.reading_value * obj.rate
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        obj.price = obj.reading.reading_value * obj.rate
        obj.save()


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'property', 'number', 'invoice_date']
    search_fields = ['number', ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'password']
    search_fields = ['email', ]

