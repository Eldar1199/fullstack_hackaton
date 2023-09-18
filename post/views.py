from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters
from .permissions import IsAuthor
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication



class PermissionMixin:
    def get_permissions(self):
        if self.action in ('create'):
            permissions = [IsAuthenticated]
        elif self.action in ('update','partial_update','destroy'):
            permissions = [IsAuthor]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]



class PostView(PermissionMixin,viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filterset_fields = ['category', 'in_stock']
    search_fields = ['vacancy','salary']


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return self.serializer_class
        

