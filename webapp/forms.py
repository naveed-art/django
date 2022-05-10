from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
                'author': forms.TextInput(attrs={'class': 'form-control','value': '', 'id': 'users_id', 'type':'hidden'} )}

        