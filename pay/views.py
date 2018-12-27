import decimal
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from pay.models import *
from new_shop.models import Product
from pay.forms import WalletForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


class Balance(View):
    """Пополнение кошелька пользователя"""

    def get(self, request):
        form = WalletForm()
        context = {
            'form': form
        }
        return render(request, 'pay/balance.html', context)

    def post(self, request):
        form = WalletForm(request.POST)
        if Wallet.objects.filter(user=request.user).exists():
            wallet = Wallet.objects.get(user=request.user)
        else:
            wallet = Wallet(user=request.user)

        if form.is_valid():
            wallet.balance += decimal.Decimal(str(float(form.cleaned_data["balance"])))
            history = History.objects.create(user=wallet, balance=wallet.balance, history=form.cleaned_data["balance"],
                                             action='3')
            history.save()
            wallet.save()
        else:
            pass
        return HttpResponseRedirect('/')


class BayView(View):
    """Покупка товара, передачи денег продавцу и комиссия портала"""

    def get(self, request, slug):
        try:
            product = Product.objects.exclude(user=request.user).get(id=slug)
        except Product.DoesNotExist:
            messages.add_message(self.request, settings.MY_INFO, 'Невозможно купить товар у себя!')
            return HttpResponseRedirect('product/{}'.format(slug))
        wallet = Wallet.objects.get(user=request.user)
        if product.price >= wallet.balance:
            messages.add_message(self.request, settings.MY_INFO, 'Недостаточно средств!')
            return HttpResponseRedirect('product/{}'.format(slug))
        elif product.price >= wallet.balance:
            messages.add_message(self.request, settings.MY_INFO, 'Недостаточно средств!')
            return HttpResponseRedirect('product/{}'.format(slug))
        wallet.balance -= decimal.Decimal(str(float(product.price)))
        percent = product.price / 100 * 20
        sell = Wallet.objects.get(user=product.user)
        sell.balance += decimal.Decimal(str(float(product.price - percent)))
        history = History.objects.create(user=wallet, balance=wallet.balance, history=product.price)
        admin_wallet = AdminWallet.objects.create(balance=percent)
        admin_wallet.save()
        history.save()
        wallet.save()
        sell.save()
        messages.add_message(self.request, settings.MY_INFO, 'Вы успешно купили товар!')
        return redirect('product/{}'.format(slug))


class HistoryView(View):
    """Вывод истории операций"""

    def get(self, request):
        history = History.objects.filter(user__user=request.user)
        context = {
            'history': history
        }
        return render(request, 'pay/history.html', context)
