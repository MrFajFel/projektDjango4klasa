from django import forms

from aplikacja.models import User,Animals

class LogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password','email')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


# {#co ma model animal = name, type, picture, animal_race, age, description, dodano, status #}
class AddAnimal(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ('name','age','type','picture','animal_race','description')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.TextInput(attrs={'class':'form-control'}),
            'picture': forms.FileInput(attrs={'class':'form-control'}),
            'animal_race': forms.TextInput(attrs={'class':'form-control'}),
             'description': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlTextarea1',
                'rows': 3
            }),
            'status':forms.Select(attrs={'class':'form-select',"aria-label":"Default select example"}),
        }