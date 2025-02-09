from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'ResetPsw/password_reset.html'
    email_template_name = 'ResetPsw/password_reset_email.html'
    subject_template_name = 'ResetPsw/password_reset_subject.txt'
    #success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        messages.success(self.request, \
                        'Email-ul pentru resetarea parolei a fost trimis. \
                        Te rugam sa verifici si folderul Spam. \
                        Dacă nu primești un email, te rugăm să verifici dacă ai introdus corect adresa cu care te-ai înregistrat', extra_tags='resetpsw_msgConfirm')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ceva nu a mers bine. Te rugam sa incerci din nou.')
        return super().form_invalid(form)