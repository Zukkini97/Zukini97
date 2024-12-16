from django.urls import path
from ResetPassword.views import ResetPasswordView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView

urlpatterns = [
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='ResetPsw/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='ResetPsw/password_reset_complete.html'),
         name='password_reset_complete'),
     path('reset-password/done', 
          PasswordResetDoneView.as_view(template_name='ResetPsw/password_reset_done.html'),
          name='password_reset_done'),
]