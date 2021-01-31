from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('pelanggan/', include('pelanggan.urls', namespace='pelanggan')),
    path('produk/', include('produk.urls', namespace='produk')),
    path('transaksi/', include('transaksi.urls', namespace='transaksi')),
]
