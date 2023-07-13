from django import forms

class PartyRegistrationForm(forms.Form):
    # Field for username
    username = forms.CharField(label='Username')

    # Field for password with password input widget
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # Field for email
    email = forms.EmailField(label='Email')
