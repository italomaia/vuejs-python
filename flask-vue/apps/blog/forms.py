from wtforms_alchemy import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        only = ['title', 'text', 'tags']
