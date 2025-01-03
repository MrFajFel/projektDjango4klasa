from django.conf.urls.static import static
from django.urls import path

from aplikacja import views
from schronisko import settings

urlpatterns = [
    path('',views.mainPage,name='mainPage'),
    path('o-nas/',views.about_us ,name='about_us'),
    path('adopcja/',views.Adopcja.as_view(),name='adopcja'),
    path('logowanie/',views.logowanie,name='login'),
    path('rejestracja/',views.register,name='register'),
    path('kontakt/',views.kontakt,name='kontakt')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)