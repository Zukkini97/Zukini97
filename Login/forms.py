from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email', 
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        error_messages={
            'required': 'Adresa de email este obligatorie.',
            'invalid': 'Adresa nu este valida.'
        }
    )
    password = forms.CharField(
        label='Parola', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Introduceti o parola.',
        }    
    )

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email.exists()):
    #         raise ValueError('Adresa este deja folosita')
    #     return email

