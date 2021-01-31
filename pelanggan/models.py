from django.db import models

# Create your models here.


class Pelanggan(models.Model):
    nama_perusahaan = models.CharField(max_length=255)
    penanggung_jawab = models.CharField(max_length=255)
    alamat = models.TextField()
    telepon = models.IntegerField()
    piutang = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.nama_perusahaan}'
