from django.db import models

# Create your models here.

class PetRecord(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
        
    ]
    
    REPRODUCTIVE_STATUS_CHOICES = [
        ('I', 'Intact'),
        ('S', 'Sterilizat'),
    
    ]

    pet_name = models.CharField(max_length=20)
    pet_species = models.CharField(max_length=20)
    pet_breed = models.CharField(max_length=20)
    pet_weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Greutatea în kg")
    pet_color_and_markings = models.CharField(max_length=50)
    pet_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pet_vaccine = models.CharField(blank=True, help_text="Vaccinările", max_length=20)
    pet_reproductive_status = models.CharField(max_length=10, choices=REPRODUCTIVE_STATUS_CHOICES)
    pet_disease = models.CharField(blank=True, help_text="Boli cronice", max_length=20)
    pet_treatments = models.CharField(blank=True, help_text="Tratamente medicale", max_length=20)
    pet_medication = models.CharField(blank=True, help_text="Medicație curentă", max_length=20)

    def __str__(self):
        return f'{self.pet_name} - {self.pet_species}'