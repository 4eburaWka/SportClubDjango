from django.contrib import admin

from .models import Client, Coach, Result


class ClientAdminModel(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'surname', 'phone_number')
    list_display_links = ('last_name', 'first_name', 'surname', 'phone_number')
    search_fields = ('last_name', 'first_name', 'surname', 'phone_number')


class CoachAdminModel(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'surname', 'phone_number', 'profile_photo')
    list_display_links = ('last_name', 'first_name', 'surname', 'phone_number', 'profile_photo')
    search_fields = ('last_name', 'first_name', 'surname', 'phone_number', 'profile_photo')


class ResultAdminModel(admin.ModelAdmin):
    list_display = ('client', 'datetime', 'value')
    list_display_links = ('client', 'datetime', 'value')
    search_fields = ('client', 'datetime', 'type_of_results', 'value')


admin.site.register(Client, ClientAdminModel)
admin.site.register(Coach, CoachAdminModel)
admin.site.register(Result, ResultAdminModel)
