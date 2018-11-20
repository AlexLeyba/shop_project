from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from new_shop.models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Q


class General(View):
    """Вывод списка товаров на главную"""

    def get(self, request):
        card = save(request)
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
        card = save(request)
        product = Product.objects.get(id=slug)
        context = {
            'product': product,
            'card': card
        }
        return render(request, "new_shop/product.html", context)


class Card_View(View):
    """корзина"""

    def get(self, request):
        card = save(request)
        context = {'card': card}
        return render(request, 'new_shop/card.html', context)


class AddCardItem(View):
    """добавление товара в корзину"""

    def get(self, request, slug):
        card = save(request)
        product = Product.objects.get(id=slug)
        card.add_to_card(slug)
        return HttpResponseRedirect('/card/')


class DeleteCardItem(View):
    """удаление товара из корзины"""

    def get(self, request, slug):
        card = save(request)
        product = Product.objects.get(id=slug)
        card.delete_to_card(slug)
        return HttpResponseRedirect('/card/')


class Category_View(View):
    """Вововд товаров по категориям"""

    def get(self, request, slug):
        card = save(request)
        category = Product.objects.filter(category__slug=slug)
        context = {'categories': category,
                   'card': card}
        return render(request, "new_shop/category.html", context)


class ProfileView(View):
    def get(self, request):
        card = save(request)
        profile = Profile.objects.get(user=request.user)
        zacaz = Zacaz.objects.filter(user=request.user)
        context = {
            'zacaz': zacaz,
            'profile': profile,
            'card': card,
        }
        return render(request, "new_shop/profile.html", context)


class ZacazView(View):
    def get(self, request):
        zacaz = Zacaz.objects.create(status=1, user=request.user, items=Card.objects.get(id=request.session['card_id']))
        card = Card()
        card.save()
        card_id = card.id
        request.session['card_id'] = card_id
        return HttpResponseRedirect('/profile/')

    def post(self, request):
        zacaz = Zacaz.objects.get(user=request.user, id=request.POST.get("pk"))
        zacaz.delete()
        return HttpResponseRedirect('/profile/')


class SearchView(View):
    """Поиск по сайту"""

    def post(self, request, *args, **kwargs):
        query = self.request.POST.get('q')
        founded = Product.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        context = {'founded': founded}
        return render(request, 'new_shop/searh.html', context)


def save(request):
    try:
        card_id = request.session['card_id']
        cards = Card.objects.get(id=card_id)
        request.session['total'] = cards.item.count()
    except:
        card = Card()
        card.save()
        request.session['card_id'] = card.id
        cards = Card.objects.get(id=card.id)
    return cards
