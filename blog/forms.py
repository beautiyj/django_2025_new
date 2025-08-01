#blog/forms.py
from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  #'author',  #아직이둘은미지정
                  'content',
                  #'category',
                  'uploaded_image',
                  'uploaded_file' ]