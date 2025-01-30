from django.contrib import admin
from user.models import User


class Users(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    list_display_links = ("username", "email")
    list_per_page = 10
    search_fields = ("username",)


admin.site.register(User, Users)
