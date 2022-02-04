from django.contrib import admin

# Register your models here.
from search_users.models import User


@admin.register(User)
class Search_Users_Admin(admin.ModelAdmin):
    list_display = ("user_id", "name", "created_at", "gold", "level", "inventory")
