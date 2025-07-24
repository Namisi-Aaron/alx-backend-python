import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    """
    User model represents a user in the application.
    """
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]

    user_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=False)
    password_hash = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')
    created_at = models.DateTimeField(auto_now_add=True)

    conversations = models.ManyToManyField('Conversation', related_name='participants', blank=True)

class Conversation(models.Model):
    """
    Conversation model represents a conversation between two users.
    """
    conversation_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('participants_id',)

class Message(models.Model):
    """
    Message model represents a message sent by a user.
    """
    message_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')