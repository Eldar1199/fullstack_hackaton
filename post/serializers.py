from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = 'company_name','vacancy','experience','salary'


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
    

    # def to_representation(self, instance):
    #     repres = super().to_representation(instance)