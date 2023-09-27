# from rest_framework.test import APITestCase, APIRequestFactory
# from django.contrib.auth import get_user_model
# from .models import ProfileUser
# from .views import ProfileUserAPIView
# # from collections import OrderedDict
# from rest_framework.authtoken.models import Token



# User = get_user_model()



# class ProfileTest(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         user = User.objects.create_user(email = 'test@gmail.com',
#                                         password = '1234',
#                                         # password_confirm = '1234',
#                                         is_active = True)
#         self.token = Token.objects.create(user=user)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
#         profile = [
#             ProfileUser(user = user, 
#                         name = 'eldar1', 
#                         surname = 'usenov1', 
#                         about_user = 'asd1'),
#         ]
#         ProfileUser.objects.bulk_create(profile)

#     def test_profile_user(self):
#         request = self.factory.get('api/v1/profile/')
#         view = ProfileUserAPIView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, 200)
#         # assert response.status_code == 200

#     def test_profile_update(self):
#         request = self.factory.patch('api/v1/profile/')
#         view = ProfileUserAPIView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, 200)
#         # assert response.status_code == 200