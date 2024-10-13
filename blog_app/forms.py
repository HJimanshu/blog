from django import forms
# from django import forms
class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    to=forms.EmailField()
    Comments=forms.CharField(required=False,widget=forms.Textarea)
    
# from django import forms
# from .models import Comment

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment']    

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment']

# class EmailPostForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     to = forms.EmailField()
#     comments = forms.CharField(required=False, widget=forms.Textarea)
