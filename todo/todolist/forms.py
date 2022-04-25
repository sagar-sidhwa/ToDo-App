from dataclasses import fields
import email
from pyexpat import model
from socket import fromshare
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from pyrsistent import field
from todolist.models import Task

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UpdateUserForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','complete')