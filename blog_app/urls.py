from django.urls import path
from .views import signup_view, login_view, blog_view, blog_post, share_post_view

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('blog/', blog_view, name='blog'),
    path('blogpost/<int:id>/', blog_post, name='blogpost'),
    # path('blogcomment/<int:blog_id>/', blog_detail_view, name='blog_detail_view'),  
    path('share/<int:id>/', share_post_view, name='share_post_view'),  
]
