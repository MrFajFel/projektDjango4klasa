from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from aplikacja.form import LogForm
from aplikacja.models import User


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
                        form.cleaned_data['nickname'] == user.username and
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
