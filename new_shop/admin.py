from django.contrib import admin
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


admin.site.register(Product, PostAdmin)
admin.site.register(Card)
admin.site.register(CardItem)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Comment)
admin.site.register(Brand)
admin.site.register(Zacaz)
admin.site.register(Profile)
