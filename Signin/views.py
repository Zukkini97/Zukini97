from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Signin.forms import SignUpForm
from django.contrib.auth.models import User

def signin(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Salvăm utilizatorul, fără să setăm un nume de utilizator, doar email-ul
            user = form.save(commit=False)
            user.username = user.email  # Setăm username la email pentru a respecta cerințele
            user.save()

            # Obținem datele introduse pentru autentificare
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # Autentificăm și conectăm utilizatorul
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Te-ai conectat cu succes!')
                return redirect('pet_record_list')
            else:
                messages.error(request, 'Autentificarea a esuat. Încearcă din nou.')
        else:
            messages.error(request, 'Formularul conține erori. Verifică informațiile și încearcă din nou.')
    

    context = {
        'form': form,
        'email_has_errors': bool(form.errors.get('email')),
        'password1_has_errors': bool(form.errors.get('password1')),
        'password2_has_errors': bool(form.errors.get('password2')),
    }

    # Reîncărcăm pagina de autentificare cu formularul (cu erori, dacă există)
    return render(request, 'Signin/signin.html', context)
