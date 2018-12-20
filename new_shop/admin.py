from django.contrib import admin
from django import forms
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from mptt.admin import MPTTModelAdmin


class ProductAdmin(admin.ModelAdmin):
    """Админка товара"""
    list_display = ("title", "date", "id")


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "date", "id")
    summernote_fields = ('text',)


class CategoryAdmin(admin.ModelAdmin):
    """подкатегория"""
    list_display = ("name", "rodcat", "slug",)


class ZacazForm(forms.ModelForm):
    class Meta:
        model = Zacaz
        fields = ("user", "status", "items")


class ZacazAdmin(admin.ModelAdmin):
    form = ZacazForm


admin.site.register(Rating)
admin.site.register(Product, PostAdmin)
admin.site.register(Card)
admin.site.register(CardItem)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Comment)
admin.site.register(Brand)
admin.site.register(Zacaz, ZacazAdmin)
admin.site.register(Profile)
