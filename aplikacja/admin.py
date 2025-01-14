from django.contrib import admin



from django.contrib import admin

from aplikacja.models import User, Animals


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

@admin.register(Animals)
class Animals(admin.ModelAdmin):
    list_display = ('id','name','type','animal_race','age','description')