from django.contrib import admin
from .models import *


class HelpAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'text', 'email', 'status')


admin.site.register(Help, HelpAdmin)
