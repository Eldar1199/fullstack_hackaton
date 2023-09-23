from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()



class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey( Post, on_delete=models. CASCADE, related_name='likes')
    
    

class Comment(models.Model):
    body = models.TextField(verbose_name='Содержимое комментария')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} {self.post.title}'
    

class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='ratings')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratings')

    def __str__(self):
        return f'{self.author} {self.rating}'
    


class FavoriteItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')


    class Meta:
        ordering: ('-pk',)
        constraints = [models.UniqueConstraint(fields=['author', 'post'], name='unique_author_post'),]
        indexes = [models.Index(fields=['author','post'], name='idx_auth_post'),]


    def __str__(self):
        return f'{self.author}->{self.post}'
    
    

# class UserFavorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
#     favorite_item = models.ForeignKey(FavoriteItem, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.username} {self.favorite_item}'

    


