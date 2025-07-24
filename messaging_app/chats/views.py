from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from chats.permissions import IsParticipantOfConversation
from .models import User, Message, Conversation
from .filters import MessageFilter
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for interacting with messages
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filterset_class = MessageFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsParticipantOfConversation]

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsParticipantOfConversation]
