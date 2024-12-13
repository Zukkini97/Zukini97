from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomAuthenticationForm


class UserLoginView(LoginView):
    template_name = 'Login/login_page.html'
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('pet_record_list')

    def get_success_url(self):
        return self.success_url

    def form_valid(self, form):
        # Autentificăm utilizatorul folosind funcția authenticate() și login()
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        remember_me = form.cleaned_data.get('remember_me')

        if user is not None:
            login(self.request, user)  # Autentificăm utilizatorul
            
            if remember_me:
                self.request.session.set_expiry(1209600) # Data de expirare dupa doua saptamani
            else:
                self.request.session.set_expiry(0)
            
            messages.success(self.request, 'Te-ai conectat cu succes!')
            return redirect(self.get_success_url())  # Redirecționăm utilizatorul
        
        else:
            messages.error(self.request, 'Adresa de email sau parola sunt incorecte!')
            return self.form_invalid(form)  # Dacă autentificarea nu a reușit, afișăm formularul invalid

    def form_invalid(self, form):
        # Când formularul este invalid, adăugăm mesaj de eroare
        messages.error(self.request, 'Te rugăm să introduci datele corecte!')
        return super().form_invalid(form)
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Te-ai deconectat cu succes!')
    return redirect('user_login')