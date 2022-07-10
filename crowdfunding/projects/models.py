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
    ('T', 'Time'),
    ('A', 'Advice'),
    ('R', 'Resources'),
    ('O', 'Other'),
]
SKILLS = [
    ('S', 'Software Development'),
    ('M', 'Marketing & Branding'),
    ('B', 'Tax/Accounting/Legal Expertise'),
    ('I', 'Industry-specific Expertise'),
    ('C', 'Events & Community Engagement'),
    ('E', 'Looking to gain work experience'),
    ('A', 'Happy to assist with whatever is needed'),
]

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField()
    description = models.TextField()
    goal = models.TextField()
    is_open = models.BooleanField()
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
    comment = models.CharField(max_length=500)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    date_created = models.DateTimeField()

