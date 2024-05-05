from django.contrib import admin
from .models import Service, SingleService, PlanVip, PlanStandart


@admin.register(Service)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'img')


@admin.register(SingleService)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'img')


@admin.register(PlanVip)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'description_ru')


@admin.register(PlanStandart)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'description_ru')
