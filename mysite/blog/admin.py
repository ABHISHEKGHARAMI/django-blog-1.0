from django.contrib import admin
from  .models import Post , Comment
# Register your models here.



# admin for the post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','status','publish']
    list_filter = ['created' ,'status', 'publish','author']
    search_fields = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status' , 'publish']
    show_facets = admin.ShowFacets.ALWAYS
    


# admin for comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','created','active']
    list_filter = ['active','created','updated']
    search_fields = ['name','body','email']
