from rest_framework.serializers import ModelSerializer
from .models import ProfileUser




class ProfileUserSerializer(ModelSerializer):
    
    class Meta:
        model = ProfileUser
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}

        