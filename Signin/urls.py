from django.urls import path
from Signin.views import signin

urlpatterns = [
    path('inregistrare/', signin, name='signin_user')
]