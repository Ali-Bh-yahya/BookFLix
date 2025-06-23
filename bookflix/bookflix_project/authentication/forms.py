from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
import datetime
#Create the Registration Form
class RegistrationForm(UserCreationForm):
   # Add extra fields here (age  and birthday)
    age = forms.IntegerField(required=True, min_value=1, max_value=120, label='Age')
    birthday = forms.DateField(required=True, label='Birthday', widget=forms.SelectDateWidget(years=range(1900, 2025)))
    class Meta:
        model = User
        fields = ['first_name','last_name','age','birthday' , 'email', 'password1', 'password2']
    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if birthday and birthday > datetime.date.today():
            raise forms.ValidationError("Birthday cannot be in the future.")
        return birthday    
    
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')