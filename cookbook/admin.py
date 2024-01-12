from django.contrib import admin

from cookbook.models import Cookbook


# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "owner")


admin.site.register(Cookbook, OrderAdmin)
