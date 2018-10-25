#доделать корзину, удаление из корзины, создание заказа, личный кабинет(отображение что с заказом)
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from new_shop.models import *
from django.core.paginator import Paginator


class General(View):
    """Вывод списка товаров на главную"""

    def get(self, request):
        product = Product.objects.all()
        paginator = Paginator(product, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, "new_shop/general.html", {"product": contacts})


class Product_View(View):
    def get(self, request, slug):
        product = Product.objects.get(id=slug)
        return render(request, "new_shop/product.html", {'product': product})


class AddCardItem(View):
    """"""
    def post(self, request):
        pk = request.POST.get("prod_id")
        product = Product.objects.get(id=pk)
        card_item = CardItem.objects.create(product=product)
        return render(request, "new_shop/product.html", {'product': product})

class Category_View(View):
    """Вововд товаров по категориям"""

    def get(self, request, slug):
        category = Product.objects.filter(category__slug=slug)
        return render(request, "new_shop/category.html", {"categories": category})
