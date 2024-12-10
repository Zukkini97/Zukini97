from django.shortcuts import render
from .forms import SearchForm
from DosareMedicale.forms import PetRecord
from django.http import JsonResponse


# Create your views here.
def search_view(request):
    results = []
    
    # Verifică dacă termenul de căutare a fost introdus
    if 'query' in request.GET:
        query = request.GET.get('query')
        results = PetRecord.objects.filter(pet_name__icontains=query)
    
    # Construiește un răspuns JSON cu rezultatele
    results_data = [
        {
            'pet_name': result.pet_name,
            'pet_species': result.pet_species,
            'pet_breed': result.pet_breed
        }
        for result in results
    ]
    
    return JsonResponse({'results': results_data})
