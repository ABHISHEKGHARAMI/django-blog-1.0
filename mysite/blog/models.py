from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class PublishManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset().filter(status=Post.Status.PUBLISHED))


class Post(models.Model):
    
    # adding the choice field for the post model 
    class Status(models.TextChoices):
        DRAFT = 'DF' ,'Draft'
        PUBLISHED = 'PB' , 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(
                            max_length=250,
                            unique_for_date='publish'
                            )
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
    # default manager for the model
    objects = models.Manager()
    # custom manager for the model
    published = PublishManager()
    
    # for the tags for the user for similar search
    tags = TaggableManager()
    
    
    # meta data for the model
    class Meta:
        ordering = ['-publish']
        indexes = models.Index(fields=['-publish']),
    
    # cannonical url for the site
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
    
    
    def __str__(self):
        return self.title
    # Admin #Admin001@
    
# creating the comment system for the user
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True)      
    
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        
    def __str__(self):
        return f"comment by {self.name} on {self.post}"
    
