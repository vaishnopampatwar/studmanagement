from django.contrib import admin

from home.models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)