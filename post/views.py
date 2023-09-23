from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters
from .permissions import IsAuthor, IsReqruiter
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from review.models import Like, FavoriteItem, Rating
from rest_framework.decorators import action
from review.serializers import LikeSerializer, FavoriteCreateSerializer, RatingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from profilee.models import ProfileUser


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('create'):
            permissions = [IsAuthenticated, IsReqruiter]
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
    # filterset_fields = []
    search_fields = ['vacancy','salary']

    def retrieve(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.views += 1
        post.save()
        serializer = self.get_serializer_class()(post)
        return Response(serializer.data, status=200)


    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = PostListSerializer
        return super().get_serializer_class()
        


    @action(methods=['POST'], detail=True,permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(post=post, author=user)
                like.delete()
                message = 'unlike'
            except Like.DoesNotExist:
                Like.objects.create(post=post, author=user)
                message = 'liked'
            return Response(message, status=201)
        

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        post = self.get_object()
        user = request.user
        serializer = FavoriteCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                fav_post = FavoriteItem.objects.get(post=post, author=user)
                fav_post.delete()
                message = 'deleted from favorites'
            except FavoriteItem.DoesNotExist:
                FavoriteItem.objects.create(post=post, author=self.request.user)
                message = 'added to favorites'
            return Response(message, status=201)
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def apply(self, request, pk=None):
        post = self.get_object()
        user_email = request.user.email
        resume = ProfileUser.objects.filter(user=request.user).first()
        user_resume = resume.user_resume.path 
        recruiter_email = post.author.email
        if post.actuality == True:
            try:
                subject = 'Отклик на ваканцию'
                message = f'Пользователь ITJOB: {user_email} отправил вам свое резюме'
                from_email = user_email
                recipient_list = [recruiter_email]

                email = EmailMessage(subject, message, from_email, recipient_list)
                email.attach_file(user_resume)
                email.send()

                return Response('Успешно отправлено', status=200)
            except Exception as e:
                return Response('Произошла ошибка при отправке электронной почты', status=500)
        else:
            return Response('ваканция не актуальна')



    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def rating(self, request, pk=None):
        post = self.get_object()
        user = request.user
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Rating.objects.create(post=post, author=user)
            return Response('Спасибо за рейтинг', status=201)

    # def perform_create(self, serializer):
    #     return serializer.save(post=self.get_object())







            



