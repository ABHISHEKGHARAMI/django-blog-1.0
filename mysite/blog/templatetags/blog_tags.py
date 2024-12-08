from django import template
from ..models import Post


register = template.Library()

@register.simple_tag
def template_tags():
    return Post.published.count()