

from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp', 'due_date')
    list_filter = ('status', 'tags')
    search_fields = ('title', 'description')

admin.site.register(Todo, TodoAdmin)

