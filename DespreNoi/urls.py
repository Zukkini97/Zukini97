from django.urls import path
from . import views

urlpatterns = [
    path('despre_noi/', views.about_us, name='about_us'),
    
]