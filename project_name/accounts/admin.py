from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):

	list_display = ['username', 'name', 'email', 'date_joined','date_updated']
	search_fields = ['username', 'name']

admin.site.register(User, UserAdmin)