from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import ProfileUser, ProfileRecruiter

User = get_user_model()


class ProfileUserSerializer(ModelSerializer):
    
    class Meta:
        model = ProfileUser
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}



class ProfileRecruiterSerializer(ModelSerializer):

    class Meta:
        model = ProfileRecruiter
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
