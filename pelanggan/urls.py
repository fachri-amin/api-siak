from django.urls import path

from .views import *

app_name = 'pelanggan'

urlpatterns = [
    path('', ListPelanggan.as_view(), name='pelanggan'),
    path('create', pelanggan_create, name='pelanggan_create'),
    path('edit/<int:id>', pelanggan_edit, name='pelanggan_edit'),
    path('delete/<int:id>', pelanggan_delete, name='pelanggan_delete'),
]
