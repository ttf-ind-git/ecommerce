from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class customerForm(ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	pincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	#photo = forms.ImageField()

	class Meta:
		model = Customer
		fields = '__all__'
			
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']