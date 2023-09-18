from rest_framework.serializers import ModelSerializer
from .models import ProfileUser, ProfileReqruiter




class ProfileUserSerializer(ModelSerializer):
    
    class Meta:
        model = ProfileUser
        fields = '__all__'

    

class ProfileReqruiterSerializer(ModelSerializer):

    class Meta:
        model = ProfileReqruiter
        fields = '__all__'
        