from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from aplikacja.form import UserRegistrationForm, LogForm
from aplikacja.models import User,Animals


class Adopcja(ListView):
    queryset =  Animals.objects.all().order_by('-dodano')
    context_object_name = 'Animals'
    paginate_by = 9
    template_name = 'strony/adopcja.html'

def mainPage(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    return render(request,'strony/stronaGlowna.html',{'cookie_exists':cookie_exists})

def about_us(request):
    return render(request,'strony/oNas.html',{'about_us':'about_us'})

# def adopcja(request):
#     return  render(request,'strony/adopcja.html', {'adopcja':'adopcja'})
def kontakt(request):
    return render(request,'strony/kontakt.html', {'kontakt':'kontakt'})


def logowanie(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    if cookie_exists:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                # Pobranie użytkownika na podstawie nazwy użytkownika
                user = User.objects.get(username=username)
                # Sprawdzenie hasła
                if check_password(password, user.password):
                    # Logowanie użytkownika (ustawienie ciasteczka lub sesji)
                    response = HttpResponseRedirect('/')  # lub reverse('app:info')
                    response.set_cookie("Zalogowany", '1')  # Ustawienie ciasteczka
                    response.set_cookie("username", user.username)  # Przechowywanie nazwy użytkownika w ciasteczku
                    return response
                else:
                    # Dodanie błędu w przypadku niepoprawnego hasła
                    form.add_error(None, "Niepoprawne dane logowania")
            except User.DoesNotExist:
                # Dodanie błędu, jeśli użytkownik nie istnieje
                form.add_error(None, "Niepoprawne dane logowania")
    else:
        form = LogForm()

    return render(request, 'logowanie_i_rejestracja/login.html', {'form': form})


def wyloguj(request):
    response = HttpResponseRedirect('/wyloguj_done/')
    response.delete_cookie('Zalogowany')
    response.delete_cookie('username')
    return response

def wyloguj_done(request):
    return render(request, 'logowanie_i_rejestracja/wyloguj.html', {'wyloguj': 'wyloguj'})
def register(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    if cookie_exists:
        return HttpResponseRedirect('/')
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