from django.contrib import admin
from .models import Customer, Expend
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username","password")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("dni","phone","money")

class ExpendAdmin(admin.ModelAdmin):
    list_display = ("start_time","end_time","user_id")

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Expend, ExpendAdmin)

