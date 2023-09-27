# from rest_framework.test import APITestCase, APIRequestFactory
# from django.contrib.auth import get_user_model
# from rest_framework.authtoken.models import Token
# from .views import RegisterUserView




# User = get_user_model()



# class UserTest(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         user = User.objects.create_user(email = 'test@gmail.com',
#                                         password = '1234',
#                                         is_active = True)
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
#         User.objects.bulk_create(user)


#     def test_user(self):
#         request = self.factory.post('api/v1/account/')
#         view = RegisterUserView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, 200)