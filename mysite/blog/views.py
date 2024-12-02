from django.shortcuts import render ,get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.

# first view for create all the get request for the posts in it
def post_list(request):
    posts = Post.objects.all()
    #try to render it
    return render(request,
                  'blog/post/list.html',{
                      'posts':posts
                  })
    
    
    
# second view for the detail of the specific post
def post_detail(request,id):
    """try:
        post = Post.objects.get(id=id)
    except Exception:
        return Http404('error occurred during the value of the data...')"""
        
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    
    return render(request,'blog/post/detail.html',{
        'post':post
    })
