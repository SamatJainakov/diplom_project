from django.contrib import admin
from .models import Vendor, Property, Payment, Meter, Reading, Usage, Cost, Invoice, Budget, User


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'address', 'city', 'region', 'phone_number', 'email']
    search_fields = ['vendor_name', 'address']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'address', 'city', 'region', 'phone_number', 'email']
    search_fields = ['vendor_name', 'address']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'payment_date', 'payment_amount']
    search_fields = ['invoice', 'payment_amount']


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'meter_location']
    search_fields = ['meter_location', ]


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ['meter', 'reading_date', 'reading_value']
    search_fields = ['reading_date', 'reading_value']


@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'meter', 'start_date', 'end_date', 'usage_amount']
    search_fields = ['usage_amount', ]


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'vendor', 'usage', 'price']
    search_fields = ['usage', 'price']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'property', 'invoice_number', 'invoice_date', 'due_date', 'amount_due']
    search_fields = ['invoice_number', ]


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'budget']
    search_fields = ['property_id', 'budget']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'password']
    search_fields = ['email', ]


