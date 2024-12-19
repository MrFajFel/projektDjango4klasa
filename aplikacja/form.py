from django import forms

from aplikacja.models import User


class LogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password','email')
        widgets = {
            'password': forms.PasswordInput(),
            'email':forms.EmailInput()
        }