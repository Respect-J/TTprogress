from django.contrib import admin

from .models import Contacts, Certificates, Mentors, UniverLogo, Hero, WhyUs, AboutMentors, Stats, About


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


@admin.register(Hero)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_top_ru', "title_bottom_ru")


@admin.register(AboutMentors)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "img")


@admin.register(Stats)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_top_ru', "title_bottom_ru")


@admin.register(WhyUs)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_top_ru', "title_bottom_ru")


@admin.register(About)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_1_ru', "img")
