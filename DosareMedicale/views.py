# Create your views here.

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, DeleteView
from django.views.generic.edit import UpdateView
from .models import PetRecord
from .forms import PetRecordForm
from django.contrib import messages

# Clasa care se ocupă de vizualizarea și completarea formularului
class PetRecordCreateView(LoginRequiredMixin, CreateView):
    model = PetRecord
    form_class = PetRecordForm
    template_name = 'Dosare_Medicale/dosare_medicale.html'
    #success_url = reverse_lazy('form_success')  # Redirect către pagina de succes

    def form_valid(self, form):
        """response = super().form_valid(form)
        # Afișează un mesaj de succes
        messages.success(self.request, 'Dosarul a fost salvat cu succes!')
        return response"""
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

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet_records = PetRecord.objects.all()  # Afișează toate formularele salvate
        context['pet_records'] = pet_records
        return context"""
    
class PetRecordListView(ListView):
    model = PetRecord
    template_name = 'Dosare_Medicale/pet_record_list.html'
    context_object_name = 'pet_records'

class PetRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = PetRecord
    template_name = 'Dosare_Medicale/pet_record_confirm_delete.html'  # Template-ul pentru confirmarea ștergerii
    context_object_name = 'petrecord'
    success_url = reverse_lazy('pet_record_list')  # Redirecționează către pagina de succes după ștergere

class PetRecordEditView(UpdateView):
    model = PetRecord
    fields = ['pet_name', 'pet_species', 'pet_breed', 'pet_weight', 'pet_color_and_markings', 
              'pet_gender', 'pet_vaccine', 'pet_reproductive_status', 
              'pet_disease', 'pet_treatments', 'pet_medication']
    template_name = 'Dosare_Medicale/edit_pet_record.html'
    success_url = reverse_lazy('pet_record_list')