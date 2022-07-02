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
class PledgeTypes (models.Model):
    pledge_types = models.CharField(max_length=20, choices=PLEDGE_TYPES)

class Categories(models.Model):
    categories = models.CharField(max_length=20, choices=CATEGORIES)

class Seeking(models.Model):
    seeking_for = models.CharField(max_length=20, choices=SKILLS)

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField()
    description = models.TextField()
    select_categories = models.ManyToManyField(Categories)
    goal = models.TextField()
    seeking = models.ManyToManyField(PledgeTypes)
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Skills(models.Model):
    skills = models.CharField(max_length=10)

class Pledge(models.Model):
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
    type = models.CharField(max_length=20, choices=PLEDGE_TYPES)
    if type=='$':
        class PledgeMoney(models.Model):
            amount = models.DecimalField(max_digits=12, decimal_places=2)
            # more code for processing payment
    if type=='T':
        class PledgeTime(models.Model):
            hours = models.DecimalField(max_digits=12, decimal_places=2)
            skill_set = models.ManyToManyField(Skills)
            name = models.CharField(max_length=100)
            email_address = models.CharField(max_length=100)
    if type=='A':
        class PledgeAdvice(models.Model):
            name = models.CharField(max_length=100)
            email_address = models.CharField(max_length=100)
    if type=='R':
        class PledgeResources(models.Model):
            resources = models.TextField()
            name = models.CharField(max_length=100)
            email_address = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
