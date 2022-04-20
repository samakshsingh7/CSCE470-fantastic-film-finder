from django.contrib import admin
from .models import Film

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

# Register your models here.

admin.site.register(Film, TodoAdmin)

# Register your models here.
