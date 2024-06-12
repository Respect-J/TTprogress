from django.contrib import admin
from .models import User


@admin.register(User)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'language')


