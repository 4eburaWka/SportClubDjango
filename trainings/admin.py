from django.contrib import admin

from trainings.models import Training, Subscription, PurchasedSubscription


class TrainingAdminModel(admin.ModelAdmin):
    list_display = ('name', 'duration', 'description', 'cost')
    list_display_links = ('name', 'duration', 'cost')
    search_fields = ('name', 'description', 'cost')


class SubscriptionAdminModel(admin.ModelAdmin):
    list_display = ('name', 'cost', 'is_active')
    list_display_links = ('name', 'cost', 'is_active')
    search_fields = ('name', 'cost', 'is_active')


class PurchasedSubscriptionAdminModel(admin.ModelAdmin):
    list_display = ('subscription', 'purchase_date', 'expiration_date', 'client')
    list_display_links = ('subscription', 'purchase_date', 'expiration_date', 'client')
    search_fields = ('subscription', 'purchase_date', 'expiration_date', 'client')


admin.site.register(Training, TrainingAdminModel)
admin.site.register(Subscription, SubscriptionAdminModel)
admin.site.register(PurchasedSubscription, PurchasedSubscriptionAdminModel)
