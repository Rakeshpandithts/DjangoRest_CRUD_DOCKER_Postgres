from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


#this models is to store assignment data.
class Assignment(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=100)
    duration = models.TimeField()
    tags = ArrayField(models.CharField(max_length=20, blank=True))
