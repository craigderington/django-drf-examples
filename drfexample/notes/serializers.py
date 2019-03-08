from rest_framework import serializers
from .models import Note, NoteTag


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    note_tags = serializers.PrimaryKeyRelatedField(many=True, queryset=NoteTag.objects.all())

    class Meta:
        model = Note
        fields = ('note_uuid', 'note_title', 'note_text', 'note_color',
                  'note_pinned', 'note_archived', 'owner', 'note_tags')


