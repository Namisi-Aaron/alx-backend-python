from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.FilterSet):
    sender_id = filters.UUIDFilter(field_name='sender_id__user_id')
    recipient_id = filters.UUIDFilter(field_name='recipient_id__user_id')
    sent_at = filters.DateTimeFromToRangeFilter()
    message_body = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Message
        fields = ['sender_id', 'recipient_id', 'sent_at', 'message_body']