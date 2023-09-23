from django.urls import path, include
from .views import CommentView, RatingView, FavoriteDeleteView, FavoriteListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comments', CommentView)
router.register('rating', RatingView)


urlpatterns = [
    path('', include(router.urls)),
    path('favorites/', FavoriteListView.as_view(), name='favorite_list'),
    path('favorites/<int:pk>/', FavoriteDeleteView.as_view(), name='delete'),
]
