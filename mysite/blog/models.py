from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class PublishManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset().filter(status=Post.status.PUBLISHED))


class Post(models.Model):
    
    
    objects = models.Manager()
    published = PublishManager()
    # adding the choice field for the post model 
    class Status(models.TextChoices):
        DRAFT = 'DF' ,'Draft'
        PUBLISHED = 'PB' , 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # adding the status field for the post publish or not default is draft
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    
    # meta data for the model
    class Meta:
        ordering = ['-publish']
        indexes = models.Index(fields=['-publish']),
    
    def __str__(self):
        return self.title
    # Admin #Admin001@
    
        
