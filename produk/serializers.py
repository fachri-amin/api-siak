from rest_framework import serializers

from .models import Produk


class ProdukSerializers(serializers.ModelSerializer):

    class Meta:
        model = Produk
        fields = ['id', 'tipe_pelumas', 'merk_pelumas',
                  'unit_base', 'stok', 'harga']
