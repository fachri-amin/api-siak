from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Pelanggan
from .serializers import PelangganSerializers

# Create your views here.


class ListPelanggan(ListAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializers
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('nama_perusahaan', 'penanggung_jawab', 'telepon')


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def pelanggan_create(request):

    if request.method == 'POST':
        serializer = PelangganSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def pelanggan_edit(request, id):
    try:
        pelanggan = Pelanggan.objects.get(id=id)
    except Pelanggan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PelangganSerializers(pelanggan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = PelangganSerializers(pelanggan)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def pelanggan_delete(request, id):
    try:
        pelanggan = Pelanggan.objects.get(id=id)
    except Pelanggan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        pelanggan.delete()
        return Response(data={'success': 'Berhasil Menghapus data pelanggan'}, status=status.HTTP_200_OK)
