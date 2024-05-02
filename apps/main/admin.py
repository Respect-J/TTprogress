from django.contrib import admin

from .models import Contacts, Certificates, Mentors, UniverLogo


@admin.register(Contacts)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('first_contact', "second_contact")


@admin.register(Certificates)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'img')


@admin.register(Mentors)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', "work_ru")


@admin.register(UniverLogo)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name_ru', "img")
