from django.contrib import admin

from .models import RusData, UzbData


@admin.register(RusData)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'date')


@admin.register(UzbData)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'date')

