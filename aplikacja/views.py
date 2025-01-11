from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView

from aplikacja.form import UserRegistrationForm, LogForm, AddAnimal
from aplikacja.models import User, Animals


class Adopcja(ListView):
    queryset = Animals.objects.all().order_by('-dodano')
    context_object_name = 'Animals'
    paginate_by = 9
    template_name = 'strony/adopcja.html'

    def dispatch(self, request, *args, **kwargs):
        admin = request.COOKIES.get('Zalogowany', 1)
        if "Zalogowany" not in request.COOKIES or "username" not in request.COOKIES:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cookie_exists'] = 'Zalogowany' in self.request.COOKIES and "username" in self.request.COOKIES
        context['username'] = self.request.COOKIES.get("username", "")
        context['admin'] = self.request.COOKIES.get('Zalogowany', 1)
        return context



def mainPage(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    admin = request.COOKIES.get('Zalogowany',1)
    return render(request,'strony/stronaGlowna.html',{'cookie_exists':cookie_exists, 'admin':admin})

def about_us(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    admin = request.COOKIES.get('Zalogowany', 1)
    return render(request, 'strony/oNas.html', {'cookie_exists':cookie_exists, 'admin':admin})

def kontakt(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    admin = request.COOKIES.get('Zalogowany', 1)
    return render(request, 'strony/kontakt.html', {'cookie_exists':cookie_exists, 'admin':admin})

def logowanie(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    if cookie_exists :
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    response = HttpResponseRedirect('/')
                    if user.admin:
                        response.set_cookie("Zalogowany", '1')
                    else:
                        response.set_cookie("Zalogowany", '0')# ustawienie ciasteczka
                    response.set_cookie("username", user.username)
                    return response
                else:
                    form.add_error(None, "Niepoprawne dane logowania")
            except User.DoesNotExist:
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


# {#('name','age','type','picture','animal_race','description') #}
def dodanieZwierzaka(request):
    cookie_exists = 'Zalogowany' and "username" in request.COOKIES
    admin = request.COOKIES.get('Zalogowany', 1)
    if admin == '0':
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = AddAnimal(request.POST,request.FILES)
        if form.is_valid():
            new_animal = Animals(
                name=form.cleaned_data['name'],
                type=form.cleaned_data['type'],
                picture=form.cleaned_data['picture'],
                animal_race = form.cleaned_data['animal_race'],
                age = form.cleaned_data['age'],
                description = form.cleaned_data['description'],
            )
            new_animal.save()
            return HttpResponseRedirect('/adopcja/')
    else:
        form = AddAnimal()
    return render(request, 'stronyAdministratora/dodajZwierzaka.html', {'form': form,'cookie_exists':cookie_exists, 'admin':admin})