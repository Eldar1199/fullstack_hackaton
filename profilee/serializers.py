from rest_framework.serializers import ModelSerializer
from .models import ProfileUser, ProfileRecruiter




class ProfileUserSerializer(ModelSerializer):
    
    class Meta:
        model = ProfileUser
        fields = '__all__'



class ProfileRecruiterSerializer(ModelSerializer):

    class Meta:
        model = ProfileRecruiter
        fields = '__all__'
        