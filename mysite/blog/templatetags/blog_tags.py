from django import template
from ..models import Post


register = template.Library()

@register.simple_tag
def total_tags():
    return Post.published.count()


@register.inclusion_tag("blog/post/latest.html")
def latest_tag(count=5):
    latest_posts = Post.published.order_by('-publish')[:5]
    
    return {
        'latest_posts': latest_posts
        
    }
