from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User 



class LoginForm(AuthenticationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Create a password',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )



class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=30,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your first name',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your last name',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your phone number (optional)',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Create a password',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
