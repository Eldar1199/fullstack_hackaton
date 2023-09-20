from .models import ProfileReqruiter, ProfileUser
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from .serializers import ProfileReqruiterSerializer, ProfileUserSerializer
# from .permissions import IsPatchRequest
from rest_framework.permissions import IsAuthenticated





# class ProfileUserView(viewsets.GenericViewSet):
#     queryset = ProfileUser.objects.all()
#     serializer_class = ProfileUserSerializer
#     permission_classes = [IsAuthenticated]

#     def list(self, request):
#         print(request.user)
#         profile = ProfileUser.objects.get(user=request.user)
#         seriializer = self.get_serializer_class()(instance=profile)
#         return Response(seriializer.data)
    
    
class ProfileUserAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        profile = self.get_object()
        serializer = ProfileUserSerializer(instance=profile)
        return Response(serializer.data)
    
    def patch(self, request):
        profile = self.get_object()
        serializer = ProfileUserSerializer(instance=profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_object(self):
        return ProfileUser.objects.get(user=self.request.user)





class ProfileReqruiterAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        profile = self.get_object()
        serializer = ProfileReqruiterSerializer(instance=profile)
        return Response(serializer.data)
    
    def patch(self, request):
        profile = self.get_object()
        serializer = ProfileReqruiterSerializer(instance=profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_object(self):
        return ProfileReqruiter.objects.get(user=self.request.user)
    