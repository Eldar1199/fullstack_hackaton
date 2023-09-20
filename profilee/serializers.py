from rest_framework.serializers import ModelSerializer
from .models import ProfileUser, ProfileReqruiter




class ProfileUserSerializer(ModelSerializer):
    
    class Meta:
        model = ProfileUser
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}



class ProfileReqruiterSerializer(ModelSerializer):

    class Meta:
        model = ProfileReqruiter
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
        