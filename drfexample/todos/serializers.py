from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    completed_date = serializers.ReadOnlyField()
    todo_uuid = serializers.ReadOnlyField()
    # owner = serializers.ReadOnlyField()

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'created_date', 'status', 'completed', 'completed_date', 'todo_uuid')
