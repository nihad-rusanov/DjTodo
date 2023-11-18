from django import forms
from django.forms import ModelForm
from .models import Todo

class RegisterForm(forms.Form):
    password = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'class':'form-control',}))
    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',}))
    

class LoginForm(forms.Form):
    password = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'class':'form-control',}))
    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',}))
    

class EditTodo(ModelForm):
    class Meta:
        model = Todo
        fields = ["content"]


