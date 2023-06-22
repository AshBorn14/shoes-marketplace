from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Username','class':'form-control mt-1'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'placeholder':'Your password','class':'form-control mt-1'}))


class SignUpForm(UserCreationForm):
    """ email = forms.EmailField(label="Email address",widget=forms.TextInput(attrs={'class':'form-control'})) """
    class Meta:
        model = User
        fields = ('username', 'email' ,'password1','password2')

    username = forms.CharField(help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>',widget=forms.TextInput(attrs={'placeholder':'Your Username','class':'form-control mt-1'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Your Email id','class':'form-control mt-1'}))
    password1 = forms.CharField(help_text ='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>',label="Password",widget=forms.TextInput(attrs={'placeholder':'password','class':'form-control mt-1'}))
    password2 = forms.CharField(help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>',label="Confirm Password",widget=forms.TextInput(attrs={'placeholder':'enter password again','class':'form-control mt-1'}))