from django.contrib import admin
from .models import Customer, Expend

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("dni","phone","money")

class ExpendAdmin(admin.ModelAdmin):
    list_display = ("start_time","end_time","user_id")

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Expend, ExpendAdmin)

