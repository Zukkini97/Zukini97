from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Cautare', max_length=100)
    