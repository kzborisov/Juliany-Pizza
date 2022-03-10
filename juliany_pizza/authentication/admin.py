from django.contrib import admin

from juliany_pizza.authentication.models import CustomUser, Profile


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (ProfileInlineAdmin,)
    list_display = ('username', 'email', 'date_joined')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name',)
    list_filter = ('user', 'first_name', 'last_name', 'user__date_joined')
