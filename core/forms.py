from django import forms
from core.models import Book

class BookForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'input input-primary'})
    )
    genre = forms.ChoiceField(
        choices=Book.GenreChoices.choices,
        widget=forms.Select(attrs={'class': 'select select-primary'})
    )