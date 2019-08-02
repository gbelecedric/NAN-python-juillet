from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import date




class team (models.Model):
    team_name = models.CharField(max_length=100)
    score = models.IntegerField()
    status = models.BooleanField()


class match (models.Model):
    one = models.CharField(max_length=200)
    two = models.CharField(max_length=200)
    coteone = models.FloatField()
    cotetwo = models.FloatField()
    finish = models.BooleanField(default=True)
    scoreone = models.IntegerField()
    scoretwo = models.IntegerField()







class bet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bet_date= models.DateField(default=date.today)
    somme = models.IntegerField(default=0)





