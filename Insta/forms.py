from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Insta.models import InstaUser


#create a new class CustomUserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        #abstractUser本来是有username 和  email ，此处多了一个profile_pic
        fields = ('username','email','profile_pic')