from django.contrib import admin
from .models import Note, NoteTag, NoteReminder


class NoteReminderInline(admin.TabularInline):
    model = NoteReminder
    extra = 0


class NoteAdmin(admin.ModelAdmin):
    list_display = ['note_title', 'note_created_date', 'owner', 'note_archived', ]
    inlines = [NoteReminderInline]

    class Meta:
        ordering = ['-id']


class NoteTagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

    class Meta:
        ordering = ['tag_name']


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteTag, NoteTagAdmin)




