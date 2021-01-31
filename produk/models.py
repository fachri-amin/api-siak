from django.db import models

# Create your models here.


class Produk(models.Model):
    tipe_pelumas = models.CharField(max_length=255)
    merk_pelumas = models.CharField(max_length=255)
    unit_base = models.CharField(max_length=255)
    stok = models.IntegerField()
    harga = models.IntegerField()

    def __str__(self):
        return f'{self.tipe_pelumas} - {self.merk_pelumas}'
