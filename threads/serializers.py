from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Message
        fields = ['id', 'content', 'timestamp', 'author']
