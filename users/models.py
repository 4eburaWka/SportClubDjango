import datetime as datetime
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

    last_name = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username


class Coach(Client):
    profile_photo = models.ImageField()


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
        return f"{self.client} {list(filter(lambda x: x[0] == self.type_of_result, ResulTypes))[1]} {self.value}"
