from django.urls import path

from .views import *

app_name = 'produk'

urlpatterns = [
    path('', ListProduk.as_view(), name='produk'),
    path('create/', produk_create, name='produk_create'),
    path('edit/<int:id>', produk_edit, name='produk_edit'),
    path('delete/<int:id>', produk_delete, name='produk_delete'),
]
