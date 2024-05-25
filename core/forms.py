from django import forms

from core.models import Contact, Payment


class ContactForm(forms.ModelForm):


    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Name'}),
            'email' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Email'}),
            'message' : forms.Textarea(attrs={'class' : 'col-lg-12', 'placeholder' : 'Message'})
        }
        

class PaymentForm(forms.ModelForm):


    class Meta:
        model = Payment
        fields = ('name', 'card_num', 'cvv', 'billing_address', 'city', 'country')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Name'}),
            'card_num' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Card Number'}),
            'cvv' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'CVV'}),
            'billing_address' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Billing Address'}),
            'city' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'City'}),
            'country' : forms.TextInput(attrs={'class' : 'col-lg-6 col-md-6', 'placeholder' : 'Country'}),
        }