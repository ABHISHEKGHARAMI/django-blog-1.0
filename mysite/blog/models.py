from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # meta data for the model
    class Meta:
        ordering = ['-publish']
        indexes = models.Index(
            fields=['-publish'],
        )
    
    def __str__(self):
        return self.title
    
        
