from django.contrib import admin

from app.models import Transaction, Wallet

admin.site.register(Transaction)
admin.site.register(Wallet)
