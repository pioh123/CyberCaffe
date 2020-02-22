from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Customer, Expend
from django.contrib.auth.models import User

#class UserAdmin(admin.ModelAdmin):
#    list_display = ("id","username","password")
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Clientes'

class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline,)
    list_display = ("id","username","password")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("dni","phone","money")

class ExpendAdmin(admin.ModelAdmin):
    list_display = ("start_time","end_time","user_id")

admin.site.unregister(User)
admin.site.register(User,UserAdmin)


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
#admin.site.unregister(User)

#admin.site.register(User, UserAdmin)
admin.site.register(Expend, ExpendAdmin)

