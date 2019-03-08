from django.contrib import admin
from .models import Note, NoteTag, NoteReminder


class NoteAdmin(admin.ModelAdmin):
    list_display = ['note_title', 'note_created_date', 'owner', 'note_archived', ]

    class Meta:
        ordering = ['-id']


class NoteTagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

    class Meta:
        ordering = ['tag_name']


class NoteReminderAdmin(admin.ModelAdmin):
    list_display = ['reminder_type', 'reminder_text', 'reminder_date', 'reminder_status']


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteTag, NoteTagAdmin)
admin.site.register(NoteReminder, NoteReminderAdmin)



