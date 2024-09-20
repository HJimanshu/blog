from django.urls import path,include
from .views import signup_view,login_view,blog_view,blog_post
urlpatterns = [
    # path('',index,name='index'),
    path('',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('blog/',blog_view,name='blog'),
    path('blogpost/<int:id>',blog_post,name='blogpost'),
]