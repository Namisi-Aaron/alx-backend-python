import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

roles = (
    ('admin', 'Admin'),
    ('guest', 'Guest'),
    ('host', 'Host')
)

# Create your models here.
class User(AbstractUser):
    """
    User Model, which extends the default Django User model.
    It includes additional fields such as:
      user_id, email, password_hash, role, and phone_number.
    """
    id = uuid.uuid4()
    user_id = models.UUIDField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    role = models.CharField(
        max_length=10,
        choices=roles,
        default='guest',
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['created_at']
    
    objects = models.Manager()

class Message(models.Model):
    """
    Message Model, which represents a message sent by a user.
    It includes fields such as:
      message_id, sender_id, message_body, and sent_at.
    """
    message_id = models.UUIDField(primary_key=True, editable=False)
    sender_id = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient_id = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender_id.username} sent at {self.sent_at}"

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['sent_at']
    
    objects = models.Manager()

class Conversation(models.Model):
    """
    Conversation Model, which represents a conversation between users.
    It includes fields such as:
      conversation_id, participants_id, and created_at.
    """
    conversation_id = models.UUIDField(primary_key=True, editable=False)
    participants_id = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id} with {self.participants_id.count()} participants"

    class Meta:
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations'
        ordering = ['created_at']
    
    objects = models.Manager()