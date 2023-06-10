from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import generic
from .forms import *

from .models import *


def user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cabinet')
    context = {'form': form}
    return render(request, 'billing/user_list.html', context)


def detail(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    context = {'form': form}
    return render(request, 'billing/private_cabinet.html', context)


def payment(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно!!!')
    context = {'form': form}
    return render(request, 'billing/payment_list.html', context)


class VendorList(generic.ListView):
    model = Vendor
    template_name = 'vendor_list.html'


class ReadingList(generic.DetailView):
    model = Reading
    template_name = 'reading_detail.html'


class CostList(generic.ListView):
    model = Cost
    template_name = 'cost_list.html'


class InvoiceList(generic.ListView):
    model = Invoice
    template_name = 'invoice_list.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['new_data'] = {'dad': 'dsadsad'}
    #     context['new_d'] = Property.objects.all()
    #     return context
