# доделать профиль,  создание заказа, отмена заказа
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from new_shop.models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


class General(View):
    """Вывод списка товаров на главную"""

    def get(self, request):
        try:
            card_id = request.session['card_id']
            card = Card.objects.get(id=card_id)
            request.session['total'] = card.item.count()
        except:
            card = Card()
            card.save()
            card_id = card.id
            request.session['card_id'] = card_id
            card = Card.objects.get(id=card_id)

        product = Product.objects.all()
        paginator = Paginator(product, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        context = {
            "product": contacts,
            'card': card
        }
        return render(request, "new_shop/general.html", context)


class Product_View(View):
    def get(self, request, slug):
        try:
            card_id = request.session['card_id']
            card = Card.objects.get(id=card_id)
            request.session['total'] = card.item.count()
        except:
            card = Card()
            card.save()
            card_id = card.id
            request.session['card_id'] = card_id
            card = Card.objects.get(id=card_id)

        product = Product.objects.get(id=slug)
        context = {
            'product': product,
            'card': card
        }
        return render(request, "new_shop/product.html", context)


class Card_View(View):
    """корзина"""

    def get(self, request):
        try:
            card_id = request.session['card_id']
            card = Card.objects.get(id=card_id)
            request.session['total'] = card.item.count()
        except:
            card = Card()
            card.save()
            card_id = card.id
            request.session['card_id'] = card_id
            card = Card.objects.get(id=card_id)

        context = {
            'card': card
        }
        return render(request, 'new_shop/card.html', context)


class AddCardItem(View):
    """добавление товара в корзину"""

    def get(self, request, slug):
        try:
            card_id = request.session['card_id']
            card = Card.objects.get(id=card_id)
            request.session['total'] = card.item.count()
        except:
            card = Card()
            card.save()
            card_id = card.id
            request.session['card_id'] = card_id
            card = Card.objects.get(id=card_id)
        product = Product.objects.get(id=slug)
        new_item = CardItem.objects.create(product=product, item_total=product.price)
        if new_item not in card.item.all():
            card.item.add(new_item)
            card.save()
            return HttpResponseRedirect('/card/')


class DeleteCardItem(View):
    """удаление товара из корзины"""

    def get(self, request, slug):
        try:
            card_id = request.session['card_id']
            card = Card.objects.get(id=card_id)
            request.session['total'] = card.item.count()
        except:
            card = Card()
            card.save()
            card_id = card.id
            request.session['card_id'] = card_id
            card = Card.objects.get(id=card_id)
        product = Product.objects.get(id=slug)
        for card_item in card.item.all():
            if card_item.product == product:
                card.item.remove(card_item)
                card.save()
                return HttpResponseRedirect('/card/')


class Category_View(View):
    """Вововд товаров по категориям"""

    def get(self, request, slug):
        category = Product.objects.filter(category__slug=slug)
        context = {
            "categories": category
        }
        return render(request, "new_shop/category.html", context)


class ProfileView(View):
    def get(self, request):
        try:
            card_id = request.session['card_id']
            card = Card.objects.get(id=card_id)
            request.session['total'] = card.item.count()
        except:
            card = Card()
            card.save()
            card_id = card.id
            request.session['card_id'] = card_id
            card = Card.objects.get(id=card_id)

        profile = Profile.objects.get(user=request.user)
        zacaz = Zacaz.objects.filter(user=request.user)
        context = {
            'zacaz': zacaz,
            'profile': profile,
            'card': card
        }
        return render(request, "new_shop/profile.html", context)


class ZacazView(View):
    def get(self, request):
        zacaz = Zacaz.objects.create(status=1, user=requset.user, items=Card.objects.get(id=request.session['card_id']))
        card = Card()
        card.save()
        card_id = card.id
        request.session['card_id'] = card_id
        return HttpResponseRedirect('/profile/')


