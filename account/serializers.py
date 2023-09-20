from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model
from .utils import send_activation_code_to_rec, send_activation_code_to_user
# from .tasks import send_activation_code_celery

User = get_user_model()

class RegisterRecruiterSerializer(ModelSerializer):
    password_confirm = CharField(min_length=4, required=True)

    class Meta:
        model  = User
        fields = ('email', 'password', 'password_confirm',)
        
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop ('password_confirm')
        if password != password_confirm:
            raise ValidationError ('Пароли не совпадают')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_recruiter(**validated_data)
        send_activation_code_to_rec(user.email, user.activation_code)
        # send_activation_code_celery.delay(user.email, user.activation_code)
        return user
    
        

class RegisterUserSerializer(ModelSerializer):
    password_confirm = CharField(min_length=4, required=True)

    class Meta:
        model  = User
        fields = ('email', 'password', 'password_confirm',)


    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop ('password_confirm')
        if password != password_confirm:
            raise ValidationError ('Пароли не совпадают')
        return attrs


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code_to_user(user.email, user.activation_code)
        # send_activation_code_celery.delay(user.email, user.activation_code)
        return user