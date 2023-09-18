from .models import ProfileReqruiter, ProfileUser
from rest_framework import viewsets
from .serializers import ProfileReqruiterSerializer, ProfileUserSerializer





class ProfileUserView(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileUserSerializer


class ProfileReqruiterView(viewsets.ModelViewSet):
    queryset = ProfileReqruiter.objects.all()
    serializer_class = ProfileReqruiterSerializer