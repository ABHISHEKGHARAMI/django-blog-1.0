from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from .models import Post
from django.http import Http404
from django.views.generic import ListView
from .forms import EmailPostForm
# Create your views here.

# first view for create all the get request for the posts in it
# def post_list(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(post_list,3)
#     page_number = request.GET.get('page',1)
#     #using try and catch block to prevention is empty page or if user try tot enter the wrong page number
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         # then goes to the page 1
#         posts = paginator.page(1)
#     #try to render it
#     return render(request,
#                   'blog/post/list.html',{
#                       'posts':posts
#                   })


# now going to use the class based views for the user
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
    
    
# second view for the detail of the specific post
def post_detail(request,year,month,day,post):
    """try:
        post = Post.objects.get(id=id)
    except Exception:
        return Http404('error occurred during the value of the data...')"""
        
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    return render(request,'blog/post/detail.html',{
        'post':post
    })


# view for the post share for the user
def post_share(request,post_id):
    # get the post using the post id
    posts = get_object_or_404(Post,
                              id=post_id,
                              status= Post.Status.PUBLISHED)
    # now go for the form data
    if request.method == 'POST':
        # get the data
        form = EmailPostForm(request.POST)
        
        if form.is_valid():
            # cleaned data
            cd = form.cleaned_data
            
            # here goes for the email sending.
            
    else:
        form = EmailPostForm()
        
    return render(request,
                  'blog/post/share.html',
                  {
                      'posts':posts,
                      'form':form
                  })