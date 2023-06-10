from django.urls import path

from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('vendor/', views.VendorList.as_view(), name='vendor'),
    path('payment/', views.payment, name='payment'),
    path('detail/', views.detail, name='detail'),
    path('invoice/', views.InvoiceList.as_view(), name='invoice_list'),
    path('reading/', views.ReadingList.as_view(), name='reading'),
    path('cost/', views.CostList.as_view(), name='cost_list'),
]
