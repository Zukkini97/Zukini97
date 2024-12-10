from django.shortcuts import render, redirect

def contact_us(request):
    return render(request, 'Home/contact.html', {})