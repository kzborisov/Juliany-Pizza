from django.contrib import admin

from juliany_pizza.authentication.models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')
    list_filter = ('user', 'first_name', 'last_name', 'user__date_joined')
