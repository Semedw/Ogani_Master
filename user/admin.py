from django.contrib import admin

from user.models import *



@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

