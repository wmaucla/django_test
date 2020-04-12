import datetime

from django.db import models
from django import forms


class Question(models.Model):  # this might have been an earlier draft that didn't get fixed, but probably should relate to the form instead. My bad!
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

