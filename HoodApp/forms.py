from .models import *
from django.forms import ModelForm
from django import forms

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','phone_number')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','phone_number','user', 'location')

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('hood_image','hood_name','description','help_line', 'location')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','hood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('business_name','business_logo','business_contact')
