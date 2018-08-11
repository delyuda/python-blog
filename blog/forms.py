from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Title here', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Post content', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'text',)
