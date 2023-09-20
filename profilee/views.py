from .models import ProfileReqruiter, ProfileUser
from rest_framework import viewsets
from .serializers import ProfileReqruiterSerializer, ProfileUserSerializer
# from .permissions import IsPatchRequest
from rest_framework.permissions import IsAuthenticated





class ProfileUserView(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileUserSerializer
    permission_classes = [IsAuthenticated]


class ProfileReqruiterView(viewsets.ModelViewSet):
    queryset = ProfileReqruiter.objects.all()
    serializer_class = ProfileReqruiterSerializer
    permission_classes = [IsAuthenticated]