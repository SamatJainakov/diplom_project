from django.urls import path

from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('vendor/', views.VendorList.as_view(), name='vendor_list'),
    path('payment/', views.payment, name='payment'),
    path('property/', views.PropertyList.as_view(), name='property_list'),
    path('invoice/', views.InvoiceList.as_view(), name='invoice_list'),
    path('usage/', views.UsageList.as_view(), name='usage_list'),
    path('cost/', views.CostList.as_view(), name='cost_list'),
]
