from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Pemesanan, Pembayaran, SuratJalan, Faktur
from .serializers import (
    PemesananSerializers,
    PemesananExpandSerializers,
    SuratJalanExpandSerializers,
    SuratJalanSerializers,
    FakturExpandSerializers,
    FakturSerializers,
    PembayaranExpandSerializers,
    PembayaranSerializers,
)
# Create your views here.

# pemesanan


class ListPemesanan(ListAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananExpandSerializers
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('pelanggan__nama_perusahaan')


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def pemesanan_create(request):

    if request.method == 'POST':
        serializer = PemesananSerializers(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
@permission_classes((IsAuthenticated,))
def pemesanan_edit(request, id):
    try:
        pemesanan = Pemesanan.objects.get(id=id)
    except Pemesanan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PemesananSerializers(
            pemesanan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = PemesananSerializers(pemesanan)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def pemesanan_delete(request, id):
    try:
        pemesanan = Pemesanan.objects.get(id=id)
    except Pemesanan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        pemesanan.delete()
        return Response(data={'success': 'Berhasil Menghapus data Pemesanan'}, status=status.HTTP_200_OK)


# surat jalan
class ListSuratJalan(ListAPIView):
    queryset = SuratJalan.objects.all()
    serializer_class = SuratJalanExpandSerializers
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('pemesanan__pelanggan__nama_perusahaan')


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def surat_jalan_create(request):

    if request.method == 'POST':
        serializer = SuratJalanSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'PATCH'])
@permission_classes((IsAuthenticated,))
def surat_jalan_edit(request, id):
    try:
        surat_jalan = SuratJalan.objects.get(id=id)
    except SuratJalan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SuratJalanSerializers(surat_jalan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SuratJalanSerializers(
            surat_jalan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = SuratJalanSerializers(surat_jalan)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def surat_jalan_delete(request, id):
    try:
        surat_jalan = SuratJalan.objects.get(id=id)
    except SuratJalan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        surat_jalan.delete()
        return Response(data={'success': 'Berhasil Menghapus data Surat Jalan'}, status=status.HTTP_200_OK)


# Faktur
class ListFaktur(ListAPIView):
    queryset = Faktur.objects.all()
    serializer_class = FakturExpandSerializers
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('pemesanan__pelanggan__nama_perusahaan')


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def faktur_create(request):

    if request.method == 'POST':
        serializer = FakturSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
@permission_classes((IsAuthenticated,))
def faktur_edit(request, id):
    try:
        faktur = Faktur.objects.get(id=id)
    except Faktur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = FakturSerializers(faktur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = FakturSerializers(faktur)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def faktur_delete(request, id):
    try:
        faktur = Faktur.objects.get(id=id)
    except Faktur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        faktur.delete()
        return Response(data={'success': 'Berhasil Menghapus data Faktur'}, status=status.HTTP_200_OK)


# pembayaran
class ListPembayaran(ListAPIView):
    queryset = Pembayaran.objects.all()
    serializer_class = PembayaranExpandSerializers
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('faktur__pemesanan__pelanggan__nama_perusahaan')


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def pembayaran_create(request):

    if request.method == 'POST':
        serializer = PembayaranSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'PATCH'])
@permission_classes((IsAuthenticated,))
def pembayaran_edit(request, id):
    try:
        pembayaran = Pembayaran.objects.get(id=id)
    except Pembayaran.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PembayaranSerializers(pembayaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = PembayaranSerializers(
            pembayaran, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = PembayaranSerializers(pembayaran)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def pembayaran_delete(request, id):
    try:
        pembayaran = Pembayaran.objects.get(id=id)
    except Pembayaran.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        pembayaran.delete()
        return Response(data={'success': 'Berhasil Menghapus data Pembayaran'}, status=status.HTTP_200_OK)
