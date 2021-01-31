from django.urls import path

from .views import *

app_name = 'transaksi'

urlpatterns = [
    path('pemesanan/', ListPemesanan.as_view(), name='pemesanan'),
    path('pemesanan/create/', pemesanan_create, name='pemesanan_create'),
    path('pemesanan/edit/<int:id>', pemesanan_edit, name='pemesanan_edit'),
    path('pemesanan/delete/<int:id>', pemesanan_delete, name='pemesanan_delete'),
    path('surat-jalan/', ListSuratJalan.as_view(), name='surat_jalan'),
    path('surat-jalan/create/', surat_jalan_create, name='surat_jalan_create'),
    path('surat-jalan/edit/<int:id>', surat_jalan_edit, name='surat_jalan_edit'),
    path('surat-jalan/delete/<int:id>',
         surat_jalan_delete, name='surat_jalan_delete'),
    path('faktur/', ListFaktur.as_view(), name='faktur'),
    path('faktur/create/', faktur_create, name='faktur_create'),
    path('faktur/edit/<int:id>', faktur_edit, name='faktur_edit'),
    path('faktur/delete/<int:id>',
         faktur_delete, name='faktur_delete'),
    path('pembayaran/', ListPembayaran.as_view(), name='pembayaran'),
    path('pembayaran/create/', pembayaran_create, name='pembayaran_create'),
    path('pembayaran/edit/<int:id>', pembayaran_edit, name='pembayaran_edit'),
    path('pembayaran/delete/<int:id>',
         pembayaran_delete, name='pembayaran_delete'),
]
