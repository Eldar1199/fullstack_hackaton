from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Post
from django.db.models import Avg
from review.serializers import CommentSerializer


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post

        fields = ['company_name','vacancy','experience','salary', 'pk']



class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_salary(self, salary):
        if salary <= 0:
            raise ValidationError(
                'Price not be 0 or little'
            )
        return salary


    def to_representation(self, instance):
        repres = super().to_representation(instance)
        repres['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        repres['likes'] = instance.likes.all().count()
        repres['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return repres

