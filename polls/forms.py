from django import forms
from .models import MessagesContacts

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = MessagesContacts
        fields = ['firstname','lastname','email', 'message']
        widgets = {
            'firstname' : forms.TextInput(attrs={ 'placeholder': "First your name", 'class': 'form-control', 'size': '20px'}),
            'lastname' : forms.TextInput(attrs={'placeholder': "Last your name", 'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'placeholder': "Enter your E-mail", 'class': 'form-control'}),
            'message' : forms.Textarea(attrs={'placeholder': "Enter your message", "rows": 5, 'class': 'form-control'}),
        }