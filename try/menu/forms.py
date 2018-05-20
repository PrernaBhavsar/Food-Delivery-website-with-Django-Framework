from django import forms
from .models import Signup

class Signup_form(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    plan = forms.CharField(max_length=100, required=False)
    class Meta:
        model = Signup
        fields = '__all__'
        exclude = ['order','total']

class Login_form(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['email','password']

class menu_form(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['order']