from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'phone_number', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.ReadOnlyField(source='sender_id.user_id')  # Output sender's UUID

    class Meta:
        model = Message
        fields = ['sender_id', 'recipient_id', 'message_body']

    def create(self, validated_data):
        """
        Automatically set sender_id to the current authenticated user.
        """
        # Ensure request.user is available in the serializer context
        user = self.context['request'].user
        if not user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to send a message.")
        validated_data['sender_id'] = user
        return super().create(validated_data)

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
