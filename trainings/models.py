from django.db import models

from users.models import Client


class Training(models.Model):
    name = models.CharField(max_length=20)
    duration = models.TimeField()
    description = models.TextField(default='')
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=20)
    available_trainings = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='subscriptions')
    cost = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PurchasedSubscription(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='purchased_subscriptions')
    purchase_date = models.DateField()
    expiration_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='purchased_subscriptions')

    def __str__(self):
        return self.subscription.name
