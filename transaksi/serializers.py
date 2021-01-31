from rest_framework import serializers

from .models import Faktur, Pembayaran, Pemesanan, SuratJalan
from pelanggan.serializers import PelangganSerializers
from pelanggan.models import Pelanggan
from produk.serializers import ProdukSerializers


class TglPengirimanSerializers(serializers.ModelSerializer):
    class Meta:
        model = SuratJalan
        fields = '__all__'


class PemesananExpandSerializers(serializers.ModelSerializer):
    pelanggan = PelangganSerializers(read_only=True)
    produk = ProdukSerializers(read_only=True)
    surat_jalan = TglPengirimanSerializers(read_only=True)

    class Meta:
        model = Pemesanan
        fields = ['id', 'pelanggan', 'tgl_pemesanan',
                  'jumlah',  'total_harga', 'produk', 'surat_jalan']


class PemesananSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pemesanan
        fields = '__all__'

    def create(self, validated_data):
        pemesanan = Pemesanan.objects.create(**validated_data)
        return pemesanan


class SuratJalanExpandSerializers(serializers.ModelSerializer):
    pemesanan = PemesananExpandSerializers(read_only=True)

    class Meta:
        model = SuratJalan
        fields = '__all__'


class SuratJalanSerializers(serializers.ModelSerializer):
    class Meta:
        model = SuratJalan
        fields = '__all__'

    def create(self, validated_data):
        surat_jalan = SuratJalan.objects.create(**validated_data)
        return surat_jalan


class FakturExpandSerializers(serializers.ModelSerializer):
    pemesanan = PemesananExpandSerializers(read_only=True)

    class Meta:
        model = Faktur
        fields = '__all__'


class FakturSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faktur
        fields = '__all__'

    def create(self, validated_data):
        faktur = Faktur.objects.create(**validated_data)
        return faktur


class PembayaranExpandSerializers(serializers.ModelSerializer):
    faktur = FakturExpandSerializers(read_only=True)

    class Meta:
        model = Pembayaran
        fields = '__all__'


class PembayaranSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = '__all__'

    def create(self, validated_data):
        pembayaran = Pembayaran.objects.create(**validated_data)
        print(pembayaran)
        return pembayaran
