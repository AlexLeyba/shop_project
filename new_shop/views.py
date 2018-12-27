from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from new_shop.forms import CommentForm, SellForm, ProfileForm
from new_shop.models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Q


class General(View):
    """Вывод списка товаров на главную"""

    def get(self, request):
        card = save(request)
        product = Product.objects.all()
        paginator = Paginator(product, 5)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        context = {
            'product': contacts,
            'card': card
        }
        return render(request, "new_shop/general.html", context)


class Product_View(View):
    """Вывод информации о продукте"""

    def get(self, request, slug):
        card = save(request)
        product = Product.objects.get(id=slug)
        comments = Comment.objects.filter(new=product.id).count()
        rating = (product.rating.star_one + product.rating.star_two + product.rating.star_three + product.rating.star_four \
                    + product.rating.star_five) / 5

        context = {
            'comments': comments,
            'product': product,
            'card': card,
            'rating': rating
        }
        return render(request, "new_shop/product.html", context)



class CommentVeiw(View):
    """Вывод отзывов о товарах"""
    def get(self,request, slug):
        card = save(request)
        product = Product.objects.get(id=slug)
        comment = Comment.objects.filter(new=product.id)
        context = {
            'product': product,
            'comment': comment,
            'card': card,
        }
        return render(request, 'new_shop/comments.html', context)




class SendCommentVeiw(View):
    def get(self, request, pk):
        form = CommentForm()
        product = Product.objects.get(id=pk)
        context = {
            'product': product,
            'form': form
        }
        return render(request, 'new_shop/sendcomment.html', context)

    def post(self, request, pk):
        """Форма отправки отзыва"""
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = Product.objects.get(id=pk)
            form.save()
            return redirect("/comments/{}".format(pk))
        else:
            pass


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
    """Профиль пользователя"""

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
    """Создание заказа"""

    def get(self, request):
        zacaz = Zacaz.objects.create(status=1, user=request.user, items=Card.objects.get(id=request.session['card_id']))
        card = Card()
        card.save()
        card_id = card.id
        request.session['card_id'] = card_id
        return HttpResponseRedirect('/accounts/profile/')

    def post(self, request):
        zacaz = Zacaz.objects.get(user=request.user, id=request.POST.get("pk"))
        zacaz.delete()
        return HttpResponseRedirect('/accounts/profile/')


class SearchView(View):
    """Поиск по сайту"""

    def post(self, request, *args, **kwargs):
        query = self.request.POST.get('q')
        founded = Product.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        context = {'founded': founded}
        return render(request, 'new_shop/searh.html', context)


def save(request):
    """Отображение корзины"""
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


class Create(CreateView):
    model = Product
    template_name = 'new_shop/sell.html'
    form_class = SellForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/accounts/profile/')

    def success_url(self):
        return redirect('/accounts/profile/')


class Update(UpdateView):
    model = Product
    template_name = 'new_shop/redit.html'
    form_class = SellForm

    # def success_url(self):
    #     return redirect("/user-product/")


class UserProduct(ListView):
    template_name = 'new_shop/update.html'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class RatingVeiw(LoginRequiredMixin,View):
    def get(self, request, pk, slug):
        product = Rating.objects.get(product__id=slug)
        if pk == 1:
            product.star_one += 1
        elif pk == 2:
            product.star_two += 1
        elif pk == 3:
            product.star_three += 1
        elif pk == 4:
            product.star_four += 1
        elif pk == 5:
            product.star_five += 1
        else:
            pass
        product.save()
        return HttpResponse(status=201)


class EditProfile(UpdateView):
    model = Profile
    template_name = 'new_shop/EditProfile.html'
    form_class = ProfileForm