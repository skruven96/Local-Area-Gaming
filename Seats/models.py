from django.db import models
from django.contrib.auth.models import User


class Seat(models.Model):
    str_id = models.CharField(max_length=3, default='Z00')
    owned_by = models.ForeignKey('Ticket', null=True, blank=True)

    def __str__(self):
        return self.str_id


class Ticket(models.Model):
    payed = models.BooleanField(default=False)
    position = models.ForeignKey(Seat, null=True, blank=True)
    owned_by = models.ForeignKey(User)
    unique_str_id = models.CharField(max_length=10)

    def __str__(self):
        return self.owned_by.username + ': ' + self.unique_str_id

