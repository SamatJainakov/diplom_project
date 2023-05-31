from .models import *
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'address', 'city', 'region', 'phone_number', 'email']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['invoice', 'payment_method', 'payment_amount']
