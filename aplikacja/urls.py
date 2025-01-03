from django.urls import path

from aplikacja import views

urlpatterns = [
    path('',views.mainPage,name='mainPage'),
    path('o-nas/',views.about_us ,name='about_us'),
    path('adopcja/',views.Adopcja.as_view(),name='adopcja'),
    path('logowanie/',views.logowanie,name='login'),
    path('rejestracja/',views.register,name='register'),
    path('kontakt/',views.kontakt,name='kontakt')
]