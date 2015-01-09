from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.TextField()
    game_id = models.ForeignKey('Game')
    members = models.ManyToManyField(User, null=True, blank=True)

    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.TextField()
    js_id = models.TextField()
    teams = models.ManyToManyField(Team, null=True, blank=True)

    def __str__(self):
        return self.name

