import datetime as datetime
from django.contrib.auth.models import User
from django.db import models


class Coach(models.Model):
    last_name = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    profile_photo = models.ImageField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"


class Client(models.Model):
    last_name = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, related_name='clients', null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"


ResulTypes = (
    (1, "Набор веса"),
    (2, "Похудение"),
    (3, "Увеличение роста")
)


class Result(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='results')
    datetime = models.DateTimeField(default=datetime.datetime.now)
    type_of_result = models.IntegerField(choices=ResulTypes)
    value = models.IntegerField()

    def __str__(self):
        return f"Результат клиента {self.client}"
