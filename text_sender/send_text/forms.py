from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class TextForm(forms.Form):
    phoneNumber = forms.CharField(label = "", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter the number you want to text here...'}) ,max_length = 13)
    textMessage = forms.CharField(label = "" , widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter the text you want to send here...'}), max_length = 1000)