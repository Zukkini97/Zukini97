from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'ResetPsw/password_reset.html'
    email_template_name = 'ResetPsw/password_reset_email.html'
    subject_template_name = 'ResetPsw/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')