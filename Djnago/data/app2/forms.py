from django import forms 

class RegisterForms(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField () #(widget=forms.PasswordInput())
    pincode = forms.IntegerField()