# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, DeleteView
from django.views.generic.edit import UpdateView
from .models import PetRecord
from .forms import PetRecordForm
from django.contrib import messages
from django.db.models.functions import Lower


# Clasa care se ocupă de vizualizarea și completarea formularului
class PetRecordCreateView(LoginRequiredMixin, CreateView):
    model = PetRecord
    form_class = PetRecordForm
    template_name = 'Dosare_Medicale/dosare_medicale.html'

    def form_valid(self, form):
        if form.is_valid:
            print(form.cleaned_data)
            form.save()
            messages.success(self.request, 'Dosarul a fost salvat cu succes!')

        else:
            print(form.errors)
            messages.error(self.request, 'A aparut o eroare la salvarea formularului!')
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('form_success', kwargs={'pk': self.object.pk})

# Clasa pentru pagina de succes (unde se vizualizează formularul salvat)
class FormSuccessView(LoginRequiredMixin, DetailView):
    template_name = 'Dosare_Medicale/form_success.html'
    model = PetRecord
    
class PetRecordListView(ListView):
    model = PetRecord
    template_name = 'Dosare_Medicale/pet_record_list.html'
    context_object_name = 'pet_records'

    def get_queryset(self):
        # Sortez alfabetic indiferent de majuscule sau minuscule direct in baza de date
        return PetRecord.objects.all().order_by(Lower('pet_name'))

def delete_pet_record(request, pk):
    # Gaseste formularul pe baza id-ului
    petrecord = get_object_or_404(PetRecord, pk=pk)

    # Verifica daca cererea este de tip POST
    if request.method == 'POST':
        petrecord.delete() # Stergem obiectul
        messages.success(request, 'Formularul a fost sters cu succes!')
        return redirect('pet_record_list')
    
    # Daca cererea nu este POST returneaza un raspuns Forbidden
    return HttpResponseForbidden()
class PetRecordEditView(UpdateView):
    model = PetRecord
    fields = ['pet_name', 'pet_species', 'pet_breed', 'pet_weight', 'pet_color_and_markings', 
              'pet_gender', 'pet_vaccine', 'pet_reproductive_status', 
              'pet_disease', 'pet_treatments', 'pet_medication']
    template_name = 'Dosare_Medicale/edit_pet_record.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Formularul a fost modificat cu succes.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('form_success', kwargs={'pk': self.object.pk})