from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        # widgets = {
        #         'author': forms.TextInput(attrs={'class': 'form-control','value': '', 'id': 'users_id', 'type':'hidden'} )}

        