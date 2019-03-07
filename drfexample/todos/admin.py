from django.contrib import admin
from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    """
    Admin class for ToDos
    """

    list_display = ['name', 'status', 'completed', 'todo_uuid']
    list_filter = ['status', 'completed']
    search_fields = ['name']

    class Meta:
        ordering = ['status', 'created_date']
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'


admin.site.register(ToDo, ToDoAdmin)
