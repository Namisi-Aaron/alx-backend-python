from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
        read_only_fields = ['user_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.CharField(source='sender.user_id', read_only=True)
    recipient_id = serializers.CharField(source='recipient.user_id', read_only=True)

    class Meta:
        model = Message
        fields = ['sender_id', 'recipient_id', 'message_body']
        read_only_fields = ['message_id', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants_id = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['participants_id', 'messages']
        read_only_fields = ['conversation_id', 'created_at']
    
    def get_participants_id(self, obj):
        return [user.user_id for user in obj.participants.all()]
    
    def get_messages(self, obj):
        return [message.message_id for message in obj.messages.all()]
