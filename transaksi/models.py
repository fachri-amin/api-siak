from django.db import models

from pelanggan.models import Pelanggan
from produk.models import Produk
# Create your models here.


class Pemesanan(models.Model):
    jumlah = models.IntegerField()
    tgl_pemesanan = models.DateField()
    total_harga = models.IntegerField(blank=True, null=True)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.total_harga = self.jumlah * self.produk.harga
        super().save()

    def __str__(self):
        return f'{self.pelanggan} - {self.produk}'


class SuratJalan(models.Model):
    tanggal = models.DateField()
    status = models.CharField(max_length=255, default='Waiting', blank=True)
    pemesanan = models.OneToOneField(
        Pemesanan, on_delete=models.CASCADE, related_name='surat_jalan')


class Faktur(models.Model):
    tgl_faktur = models.DateField()
    tgl_jatuh_tempo = models.DateField()
    lunas = models.IntegerField(default=0, null=True, blank=True)
    pemesanan = models.OneToOneField(Pemesanan, on_delete=models.CASCADE)


class Pembayaran(models.Model):
    jumlah_bayar = models.IntegerField()
    tgl_pembayaran = models.DateField()
    status = models.CharField(
        max_length=255, default='Waiting', blank=True, null=True)
    faktur = models.ForeignKey(Faktur, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.status == 'complete' or self.status == 'Complete':
            self.faktur.lunas += self.jumlah_bayar
            self.faktur.save()

        super().save()

    def __str__(self):
        return f'{self.faktur.pemesanan} - {self.jumlah_bayar}'
