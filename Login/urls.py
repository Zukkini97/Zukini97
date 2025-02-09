from django.urls import path
from . import views
from Login.views import UserLoginView, logout_user
from DosareMedicale.views import PetRecordCreateView, FormSuccessView


urlpatterns = [
    path('autentificare/', UserLoginView.as_view(), name='user_login'),
    path('dosare_medicale/', PetRecordCreateView.as_view(), name='dosare_medicale'),
    path('form_success/', FormSuccessView.as_view(), name='form_success'),
    path('deconectare/', views.logout_user, name='logout')
]