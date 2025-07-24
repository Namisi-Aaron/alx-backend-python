from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
        read_only_fields = ['user_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.ReadOnlyField(source='sender.user_id')
    recipient_id = serializers.ReadOnlyField(source='recipient.user_id')

    class Meta:
        model = Message
        fields = ['sender_id', 'recipient_id', 'message_body']
        read_only_fields = ['message_id', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants_id = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['participants_id', 'messages']
        read_only_fields = ['conversation_id', 'created_at']
