from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , Profile
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model=User
    list_display= ('email' , 'is_staff' , 'is_active' , 'is_superuser')
    list_filter = ('email' , 'is_superuser' , 'is_active' ,)
    searching_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {
            'fields': (
                'email', 'password',
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_superuser', 'is_active'
            ),
        }),
        ('Group Permissions', {
            'fields': (
                'groups', 'user_permissions'
            ),
        }),
        ('Importent Dates', {
            'fields': (
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        (None , {
            'classes' : ('wide',),
            'fields' : ('email', 'password1' , 'password2' , 'is_staff' , 'is_active' ,'is_superuser')
        }),
    )

admin.site.register(Profile)
admin.site.register(User , CustomUserAdmin)

