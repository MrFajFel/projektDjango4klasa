from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from aplikacja.form import UserRegistrationForm, LogForm
from aplikacja.models import User
from django.shortcuts import render



def mainPage(request):
    return render(request,'strony/stronaGlowna.html',{'mainPage':'mainPage'})

def about_us(request):
    return render(request,'strony/oNas.html',{'about_us':'about_us'})

def adopcja(request):
    return  render(request,'strony/adopcja.html', {'adopcja':'adopcja'})


def logowanie(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            #Sprawdzenie danych logowania
            for user in User.objects.all():

                if (
                        form.cleaned_data['username'] == user.username and
                        check_password(form.cleaned_data['password'], user.password)
                ):
                    # Tworzenie odpowiedzi z przekierowaniem
                    response = HttpResponseRedirect('/')  # lub reverse('app:info')
                    response.set_cookie("Zalogowany", '1')  # Ustawienie ciasteczka
                    return response

            #Jeśli dane logowania są niepoprawne, przekaż błąd
            form.add_error(None, "Niepoprawne dane logowania")

    else:
        form = LogForm()

    return render(request, 'logowanie_i_rejestracja/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Utworzenie nowego użytkownika na podstawie formularza
            new_user = User(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password']),
                email=form.cleaned_data['email']
            )
            new_user.save()
            return render(request, 'logowanie_i_rejestracja/register_done.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'logowanie_i_rejestracja/rejestracja.html', {'form': form})