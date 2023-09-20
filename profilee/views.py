from .models import ProfileRecruiter, ProfileUser
from rest_framework import viewsets
from .serializers import ProfileRecruiterSerializer, ProfileUserSerializer
# from .permissions import IsPatchRequest
from rest_framework.permissions import IsAuthenticated





class ProfileUserView(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileUserSerializer
    permission_classes = [IsAuthenticated]


class ProfileRecruiterView(viewsets.ModelViewSet):
    queryset = ProfileRecruiter.objects.all()
    serializer_class = ProfileRecruiterSerializer
    permission_classes = [IsAuthenticated]