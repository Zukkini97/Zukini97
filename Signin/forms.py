from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.password_validation import CommonPasswordValidator


class SignUpForm(UserCreationForm):
    # Definim câmpuri pentru email și parole, eliminăm username-ul
    email = forms.EmailField(
        label='', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa Email*'}),
        error_messages={
            'required': 'Adresa de email este obligatorie.',
            'invalid': "Adresa nu este valida."
        }
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        error_messages={
            'required': 'Introduceți o parolă.',
            'min_length': 'Cel putin 8 caractere sunt necesare..'
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Confirmați parola.'
        }
    )

    # Elimimăm câmpul 'username' deoarece înregistrarea va fi pe baza emailului
    username = None

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')  # Folosim doar email și parolele
        # error_messages = {
        #     'email': {
        #         'unique': 'Aceasta adresa de email este deja folosita.',
        #         'required': 'Adresa de email este obligatorie.',
        #     },
        # }

    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Stilizăm câmpul email
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['email'].label = ''
        
        # Stilizăm câmpurile pentru parole
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password1'].label = ''
        
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].label = ''
        

    # Validare pentru email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Adresa este deja folosita!')
        return email

    # Validare pentru Parola si Confirmare Parola   
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise ValidationError('Campul acesta este obligatoriu!')
        if len(password1) < 8:
            raise ValidationError('Parola trebuie sa contina minim 8 caractere!')
        if password1.isdigit():
            raise ValidationError('Parola nu poate fi alcatuita numai din cifre!')
        if not re.search(r'[A-Z]', password1):
            raise ValidationError('Parola trebuie sa contina cel putin o litera mare!')
        common_validator = CommonPasswordValidator()
        try:
            common_validator.validate(password1)
        except ValidationError:
            raise ValidationError('Parola este prea comuna. Alege o parola mai complexa!')
        return password1

    # Validare pentru Confirmare Parola
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise ValidationError('Campul acesta este obligatoriu!')

        # Verificăm doar dacă parolele coincid
        if password1 != password2:
            raise ValidationError('Cele doua parole nu coincid!')
        
        return password2
