from django import forms

from .models import GuestBook


class RecordForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['author', 'email', 'description']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control mb-3'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-3'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3'
            })
        }
