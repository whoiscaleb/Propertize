from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Property, Showing, Favorite


# Register your models here.
admin.site.register(Property)
admin.site.register(Showing)
admin.site.register(Favorite)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "first_name", "last_name"]

admin.site.register(CustomUser, CustomUserAdmin)