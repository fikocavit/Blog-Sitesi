from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel
# Register your models here.


class CustomAdmin(UserAdmin):
    search_fields=['user','email']
    fieldsets =UserAdmin.fieldsets+ (
        ("Avatar Olusturma Alani", {
            "fields": ['avatar'],
        }),
    )


admin.site.register(CustomUserModel,CustomAdmin)