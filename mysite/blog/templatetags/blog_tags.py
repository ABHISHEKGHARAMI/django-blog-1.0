from django import template
from ..models import Post
from django.db.models import Count


register = template.Library()

@register.simple_tag
def total_tags():
    return Post.published.count()


@register.inclusion_tag("blog/post/latest_post.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:5]
    
    return {
        'latest_posts': latest_posts
        
    }
    
    
# recommend for tags for most commend tag
@register.simple_tag
def get_recommend_posts(count=5):
    return Post.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:5]

