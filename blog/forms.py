from django import forms
from . import models


class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['image', 'headline', 'author', 'blog_text']