from rest_framework import serializers

from .models import Pelanggan


class PelangganSerializers(serializers.ModelSerializer):

    class Meta:
        model = Pelanggan
        fields = ['id', 'nama_perusahaan', 'penanggung_jawab',
                  'alamat', 'telepon', 'piutang']
