from django.contrib import admin

# Register your models here.

from django.contrib import admin
from sign.models import Event, Guest


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', 'id', 'create_time']
    search_fields = ['name'] # 搜索栏
    list_filter = ['status'] # 过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event', 'create_time']
    search_fields = ['realname', 'phone']
    list_filter = ['sign']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)