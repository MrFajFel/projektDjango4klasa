from django.urls import path

from aplikacja import views

urlpatterns = [
    path('',views.mainPage,name='mainPage'),
    path('o-nas/',views.about_us ,name='about_us'),
    path('adopcja/',views.adopcja,name='adopcja'),
    path('logowanie/',views.logowanie,name='login')
]