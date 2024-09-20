from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
class Blogpost(models.Model):
    STATUS_CHOICES = (('draft', 'draft'),(  'published', 'published'),)
    blog_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags=TaggableManager()
    
    def __str__(self):
        return self.title
  

# class Tag(models.Model):
#     name=models.CharField(max_length=100,unique=True) 
#     def __str__(self):
#         return self.name  
    
class Blogpost_tag(models.Model):
   
    blog_post=models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    
class Comment(models.Model):   
    com_id=models.AutoField(primary_key=True) 
    comment=models.TextField()
    written_by=models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post=models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.comment
class Like(models.Model):
    like_count = models.CharField(max_length=10,default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)   
 
    def __str__(self):
        return self.like_count     