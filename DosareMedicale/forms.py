from django import forms
from .models import PetRecord

class PetRecordForm(forms.ModelForm):
    pet_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nume', 'class': 'form-control'}), label='')
    pet_species = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Specie', 'class': 'form-control'}), label='')
    pet_breed = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Rasa', 'class': 'form-control'}), label='')
    pet_weight = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Greutate (kg)', 'class': 'form-control'}), label='')
    pet_color_and_markings = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Culoare', 'class': 'form-control'}), label='')
    
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    pet_gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='Gen')

    pet_vaccine = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Vaccin', 'class': 'form-control'}), label='')
    
    REPRODUCTIVE_STATUS_CHOICES = [
        ('I', 'Intact'),
        ('S', 'Sterilizat'),
    ]
    pet_reproductive_status = forms.ChoiceField(required=True, choices=REPRODUCTIVE_STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='Statusul reproductiv')

    pet_disease = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Boli', 'class': 'form-control'}), label='')
    pet_treatments = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Tratamente', 'class': 'form-control'}), label='')
    pet_medication = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Medicatii', 'class': 'form-control'}), label='')

    class Meta:
        model = PetRecord
        fields = '__all__'