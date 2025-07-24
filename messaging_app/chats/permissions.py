from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.participants.filter(id=request.user.id).exists()