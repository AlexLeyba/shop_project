from django.contrib import admin
from pay.models import Wallet, AdminWallet, History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'history', 'balance', 'date')


class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance', 'percent')
    list_editable = ['percent']


admin.site.register(Wallet)
admin.site.register(AdminWallet, WalletAdmin)
admin.site.register(History, HistoryAdmin)
