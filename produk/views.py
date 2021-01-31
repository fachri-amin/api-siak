from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Produk
from .serializers import ProdukSerializers

# Create your views here.


class ListProduk(ListAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializers
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('tipe_pelumas', 'merk_pelumas', 'unit_base')


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def produk_create(request):

    if request.method == 'POST':
        serializer = ProdukSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
@permission_classes((IsAuthenticated,))
def produk_edit(request, id):
    try:
        produk = Produk.objects.get(id=id)
    except Produk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProdukSerializers(produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = ProdukSerializers(produk)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def produk_delete(request, id):
    try:
        produk = Produk.objects.get(id=id)
    except Produk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        produk.delete()
        return Response(data={'success': 'Berhasil Menghapus data Produk'}, status=status.HTTP_200_OK)
