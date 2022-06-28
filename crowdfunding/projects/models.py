from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.TextField()
    image = models.FileField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

PLEDGE_TYPES = [
    ('$', 'Money'),
    ('T', 'Time'),
    ('A', 'Advice'),
    ('R', 'Resources'),
    ('O', 'Other'),
]
class Pledge(models.Model):
    type = models.CharField(max_length=20, choices=PLEDGE_TYPES)
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
