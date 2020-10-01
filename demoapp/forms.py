from django.core import validators
from django import forms
from django.contrib.auth.models import User
from demoapp.models import UserProfileInfo



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField( label="enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

def clean(self):
    all_clean_data = super().clean()
    mail = all_clean_data["email"]
    check = all_clean_data["verify_email"]
    if mail != check:
        raise forms.ValidationError("make sure emails match")

    else:
        print("successfully registered")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserprofileInfoFrom(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')