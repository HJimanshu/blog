from django.contrib import admin
from django.contrib.auth.models import User
from .models import Blogpost,Blogpost_tag,Comment,Like 
# Register your models here.
class BlogpostAdmin(admin.ModelAdmin):
    list_display=['blog_id', 'title', 'author']
    ordering =('blog_id',)
    list_filter=('title',)
    search_fields=('tags',)
    list_per_page=5
    
admin.site.register(Blogpost,BlogpostAdmin)
class Blogpost_tagAdmin(admin.ModelAdmin):
    list_display=['blog_post']
    # search_fields=('tags',)
    # list_filter=('title',)
    list_per_page=50
    
admin.site.register(Blogpost_tag,Blogpost_tagAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display=['com_id', 'comment', 'written_by', 'blog_post',]
    list_filter=('blog_post',)
    
admin.site.register(Comment,CommentAdmin)
class LikeAdmin(admin.ModelAdmin):
    list_display=['like_count', 'user', 'comment']
    list_filter=('comment',)
admin.site.register(Like,LikeAdmin)