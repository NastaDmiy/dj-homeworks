from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Регистрируем модель Token в админке
admin.site.register(Token)

# Добавляем токен в отображение пользователя
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)