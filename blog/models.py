from django.db import models
from django.utils import timezone

# Create your models here.

class blog(models.Model):
    question = models.CharField(max_length=200)
    sausage = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__ (self):
        return self.question
    
class posts(models.Model):
    CreatorId = models.BigIntegerField()
    CategoryId = models.IntegerField()
    Image = models.URLField(max_length=255)
    Title = models.CharField(max_length=255)
    Body = models.TextField()
    Tags = models.CharField(max_length=255)
    DateCreated = models.DateTimeField('date published')
    Active = models.BooleanField()
    
class comments(models.Model):
    PostId = models.BigIntegerField()
    PostedFromIP = models.IPAddressField()
    CreatorName = models.CharField(max_length=255)
    CreatorURL = models.URLField(max_length=255)
    Image = models.URLField(max_length=255)
    Body = models.TextField()
    DateCreated = models.DateTimeField('date published')
    Active = models.BooleanField()