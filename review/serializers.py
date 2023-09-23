from rest_framework.serializers import ModelSerializer,ReadOnlyField,ValidationError
from .models import Comment, Like, Rating,FavoriteItem
# from post.serializers import PostListSerializer



class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create( author=user, **validated_data)
        return comment        





class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Rating
        fields = '__all__'


    def validate_rating(self, rating):
        if rating in range(1,6):
            return rating
        raise ValidationError('Рейтинг должен быть от 1 до 5')
    
    # def validate_post(self,post):
    #     user = self.context.get('request').user
    #     if self.Meta.model.objects.filter(post=post,author=user).exists():
    #         raise ValidationError('Вы уже оставляли рейтинг')
    #     return post
    
    # def validate_post_author(self,author):
    #     # user = self.context.get('request').user
    #     if author == self.context.get('request').post.author:
    #         raise ValidationError('Автор не может поставить рейтинг на свой пост')
    #     return author

    
    # def create(self, validated_data):
    #     user = self.context.get('request').user
    #     return self.Meta.model.objects.create(author=user, **validated_data)




class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    post = ReadOnlyField(source='')


    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)
    


class FavoriteListSerializer(ModelSerializer):
    # post = PostListSerializer

    class Meta:
        model = FavoriteItem
        fields = '__all__'


class FavoriteCreateSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = FavoriteItem
        fields = ('post', 'author')


