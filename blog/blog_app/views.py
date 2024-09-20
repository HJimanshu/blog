from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Blogpost

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # First, validate that the user existance
        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, "User already exists")
            return render(request, 'app/signup.html', {'msg': message})

        # Validate password in runtime
        if password1 != password2:
            messages.error(request, "Password and Confirm Password do not match")
            return render(request, 'app/signup.html', {'msg': message})

        # Create the user
        newuser = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "User registered successfully")
        return redirect('login') 

    return render(request, 'app/signup.html')

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not username or not password:
            messages.error(request,"Username and Password are required")
            return render(request, 'app/login.html')
        else:
            #authenticate the user
            user=authenticate(request,username=username, password=password)
            if user is not None:
                messages.success(request,"Login successful")
                return redirect('blog')
            messages.error(request,"invalid user credentials")
                
        return render(request,'app/login.html')  
    return render(request, 'app/login.html')
    
    
def blog_view(request):
    post=Blogpost.objects.all()[:6]
    # pritn(post)
    data={
        'posts': post
    }
    return render(request, 'app/blog.html',data)
def blog_post(request,id):
    post=Blogpost.objects.get(blog_id=id)
    return render(request, 'app/blog_post.html',{'post':post})