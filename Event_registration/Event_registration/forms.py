from django import forms

TEXT_INPUT = forms.TextInput(attrs={'class':'input','placeholder':'Enter Value'})

class TicketForm(forms.Form):
    name = forms.CharField(min_length = 2, widget=TEXT_INPUT)
    email = forms.EmailField(min_length = 5, widget=TEXT_INPUT)
    phone = forms.CharField(min_length=11, max_length=11, widget=TEXT_INPUT)
