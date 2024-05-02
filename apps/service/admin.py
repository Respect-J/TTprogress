from django.contrib import admin
from .models import Service, SingleService


@admin.register(Service)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'img')


@admin.register(SingleService)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('plan_vip_ru', 'plan_standar_ru')

