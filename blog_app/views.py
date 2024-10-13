from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Blogpost,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import EmailPostForm

from django.core.mail import send_mail
# signup form
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
            return render(request, 'app/signup.html', {'msg': messages})

        # Validate password in runtime
        if password1 != password2:
            messages.error(request, "Password and Confirm Password do not match")
            return render(request, 'app/signup.html', {'msg': message})

        # Create the user
        newuser = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "User registered successfully")
        return redirect('login') 

    return render(request, 'app/signup.html')
#login authentication
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
    
# throug this view blog are listed 
def blog_view(request):
    # Adding the tagging functionality in models.py and searching based on tags 
    tag = request.GET.get('tag')  # Get the tag from the URL
    if tag:
        post = Blogpost.objects.filter(tags__name__in=[tag])
    else:
        post=Blogpost.objects.all()
        
    paginator=Paginator(post,5)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
            
    # pritn(post)
    data={
        'posts': posts,'tag': tag,
    }
    return render(request, 'app/blog.html',data)
#Through this view we can see a single blog by id(Blog are detailed)
def blog_post(request,id):
    post=Blogpost.objects.get(blog_id=id)
    return render(request, 'app/blog_post.html',{'post':post})



# def blog_detail_view(request, blog_id):
#     post = get_object_or_404(Blogpost, pk=blog_id)
#     comments = Comment.objects.filter(blog_post=post)
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog_post = post
#             comment.written_by = request.user
#             comment.save()
#             return redirect('blog_detail', blog_id=post.blog_id)
#     else:
#         form = CommentForm()

#     context = {
#         'post': post,
#         'comments': comments,
#         'form': form,
#     }
#     return render(request, 'app/comment.html', context)

# def share_post_view(request, id):
#     post = get_object_or_404(Blogpost, blog_id=id)
#     sent = False
#     if request.method == 'POST':
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = f"{cd['username']} recommends you read {post.title}"
#             message = f"Read {post.title} at {post_url}\n\n{cd['username']}\'s comments: {cd['comments']}"
#             send_mail(subject, message, 'exampledjango12@gmail.com', [cd['to']])
#             sent = True
#             return redirect('blog_detail_view', blog_id=post.blog_id)  # Redirect to a valid view
#     else:
#         form = EmailPostForm()
#     return render(request, 'app/share.html', {'form': form, 'post': post, 'sent': sent})


# def blog_detail_view(request, blog_id):
#     post = get_object_or_404(Blogpost, pk=blog_id)
#     comments = Comment.objects.get(com_id=post)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.com_id = post
#             comment.written_by = request.user
#             comment.save()
#             return redirect('blog_detail_view', com_id=post.blog_id)
#     else:
#         form = CommentForm()

#     context = {
#         'post': post,
#         'comments': comments,
#         'form': form,
#     }
#     return render(request, 'app/comment.html', context)

def share_post_view(request, id):
    post = get_object_or_404(Blogpost, blog_id=id)
    # post=Blogpost.objects.get(blog_id=id)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())  # Ensure this method exists in your Blogpost model
            subject = f"{cd['username']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['username']}'s comments: {cd['comments']}"
            try:
                send_mail(subject, message, 'exampledjango12@gmail.com', [cd['to']])
                sent = True
                return redirect('blog_detail_view', blog_id=post.blog_id)  # Ensure this view exists
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")

    else:
        form = EmailPostForm()

    return render(request, 'app/share.html', {'form': form, 'post': post, 'sent': sent})
