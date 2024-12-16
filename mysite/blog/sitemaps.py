from django.contrib.sitemaps import Sitemap
from .models import Post


# creating the site map 
class PostSiteMap(Sitemap):
    changefreq = 'weekly'
    priority  = 0.9
    
    def items(self):
        return Post.published.all()
    
    def lastMob(self,obj):
        return obj.updated
    
    