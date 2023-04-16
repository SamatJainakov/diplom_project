from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Vendor, Property, Payment, Meter, Reading, Usage, Cost, Invoice, Budget, User


class Login(generic.ListView):
    model = User
    template_name = 'user_list.html'


class VendorList(generic.ListView):
    model = Vendor
    template_name = 'vendor_list.html'


class PropertyList(generic.ListView):
    model = Property
    template_name = 'property_list.html'


class PaymentList(generic.ListView):
    model = Payment
    template_name = 'payment_list.html'


class MeterList(generic.DetailView):
    model = Meter
    template_name = 'meter_detail.html'


class ReadingList(generic.DetailView):
    model = Reading
    template_name = 'reading_detail.html'


class UsageList(generic.ListView):
    model = Usage
    template_name = 'usage_list.html'


class CostList(generic.ListView):
    model = Cost
    template_name = 'cost_list.html'


class InvoiceList(generic.ListView):
    model = Invoice
    template_name = 'invoice_list.html'


class BudgetList(generic.DetailView):
    model = Budget
    template_name = 'budget_detail.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['new_data'] = {'dad': 'dsadsad'}
    #     context['new_d'] = Property.objects.all()
    #     return context
