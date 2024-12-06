from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'timestamp', 'title', 'description', 'due_date', 'tags', 'status']
