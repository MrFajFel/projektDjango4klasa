from django.conf.urls.static import static
from django.urls import path

from aplikacja import views
from schronisko import settings

urlpatterns = [
    path('',views.mainPage,name='mainPage'),
    path('o-nas/',views.about_us ,name='about_us'),
    path('adopcja/',views.Adopcja.as_view(),name='adopcja'),
    path('logowanie/',views.logowanie,name='login'),
    path('wyloguj/',views.wyloguj,name='wyloguj'),
    path('wyloguj_done/',views.wyloguj_done,name='wyloguj_done'),
    path('rejestracja/',views.register,name='register'),
    path('kontakt/',views.kontakt,name='kontakt'),
    path('dodajZwierzaka/',views.dodanieZwierzaka,name='dodajZwierzaka'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)