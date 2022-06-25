from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.TextField()
    image = models.FileField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
    supporter = models.CharField(max_length=200)
