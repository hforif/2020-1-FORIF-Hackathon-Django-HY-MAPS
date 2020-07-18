from django.db import models
from maps.models import Building
# Create your models here.


class BuildingPhoto(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    url = models.TextField(default="", blank=True)
