from django.urls import path

from aplikacja import views

urlpatterns = [
    path('',views.mainPage,name='mainPage')
]