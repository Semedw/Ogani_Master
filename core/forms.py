from django import forms

from core.models import Contact


class ContactForm(forms.ModelForm):


    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Name'}),
            'email' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Email'}),
            'message' : forms.Textarea(attrs={'class' : 'col-lg-12', 'placeholder' : 'Message'})
        }
        
