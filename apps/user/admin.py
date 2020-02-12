from django.contrib import admin
from .models import User, Expend

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","dni","phone","money","register")

class ExpendAdmin(admin.ModelAdmin):
    list_display = ("start_time","end_time","user_id")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Expend, ExpendAdmin)

