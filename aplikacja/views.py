from django.shortcuts import render, redirect


def mainPage(request):
    return render(request,'strony/stronaGlowna.html',{'mainPage':'mainPage'})


# Create your views here.
