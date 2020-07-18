from django.db import models

# Create your models here.


class Building(models.Model):
    number = models.IntegerField(primary_key=True)
    cv_store = models.TextField(default="", blank=True)
    cafe = models.TextField(default="", blank=True)
    lounge = models.TextField(default="", blank=True)
    portal = models.TextField(default="", blank=True)
    portal_video = models.TextField(default="", blank=True)
    department = models.TextField(default="", blank=True)
    one_line = models.TextField(default="", blank=True)
    cafeteria = models.TextField(default="", blank=True)
