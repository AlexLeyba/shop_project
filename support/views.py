from django.shortcuts import render
from support.forms import SupForm
from support.models import *
from django.views.generic import View
from new_shop.views import *
from django.contrib import messages
from django.http import HttpResponseRedirect


class HelpView(View):
    """Обратная связь"""
    def get(self, request):
        card = save(request)
        form = SupForm()
        context = {
            'form': form,
            'card': card
        }
        return render(request, 'support/form.html', context)


class HelpForm(View):
    """Отправка формы """
    def post(self, request):
        form = SupForm(request.POST)
        if form.is_valid():
            isinstance = form.save()
            messages.success(request, 'Ваш запрос успешно отправлен!')
            return HttpResponseRedirect('/support/')
        else:
            pass
