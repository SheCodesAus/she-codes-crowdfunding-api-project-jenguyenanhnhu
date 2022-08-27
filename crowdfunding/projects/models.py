from django.db import models
from django.contrib.auth import get_user_model

CATEGORIES = [
    ('1', 'Technology'),
    ('2', 'Environment or Sustainability'),
    ('3', 'Education'),
    ('4', 'Diversity & Inclusion'),
    ('5', 'Community Building & Events'),
    ('6', 'Human Rights'),
    ('7', 'International'),
    ('8', 'Other'),
]
PLEDGE_TYPES = [
    ('$', 'Money'),
    ('Time', 'Volunteering Time'),
    ('Advice', 'Advice'),
    ('Resources', 'Resources'),
    ('Other', 'Other'),
]

PROGRESS_TRACKER = [
    ('Ideation', 'Ideation Stage'),
    ('Need Funds', 'Fundraising and accepting all forms of help'),
    ('Behind', 'Behind'), 
    ('On Track', 'On Track'),
    ('Ahead of Schedule', 'Ahead of Schedule'),
    ('Complete', 'Complete'),
    ('Abandoned', 'Abandoned'),
]
class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField()
    is_technology = models.BooleanField()
    is_sustainability = models.BooleanField()
    is_education = models.BooleanField()
    is_diversity = models.BooleanField()
    is_health = models.BooleanField()
    is_human_rights = models.BooleanField()
    is_other = models.BooleanField()
    description = models.TextField()
    goal = models.TextField()
    progress = models.CharField(max_length=20, choices=PROGRESS_TRACKER)
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Pledge(models.Model):
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
    type = models.CharField(max_length=20, choices=PLEDGE_TYPES)
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

class Post(models.Model):
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
    title = models.CharField(max_length=200)
    image = models.FileField()
    progress = models.CharField(max_length=20, choices=PROGRESS_TRACKER)
    message = models.TextField()
    date_created = models.DateTimeField()
    next_update = models.DateField()

