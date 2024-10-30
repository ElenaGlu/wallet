from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/wallets/<uuid:wallet_id>/operation/', views.update_wallet, name='update_wallet'),
    path('api/v1/wallets/<uuid:wallet_id>/', views.get_wallet, name='get_wallet'),
]
