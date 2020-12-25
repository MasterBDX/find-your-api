from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from ..serializers import UserApiSerializer
from apis.models import UserApiModel

from datetime import date

def create_user(data):
    return UserApiModel.objects.create(**data)


class TestViews(TestCase):
    def setUp(self):
        self.data = {'first_name':'Test first',
                      'last_name':'Test last',
                      'full_name':'Test Full Name',
                      'username':'Test Username',
                      'gender':'male',
                      'birthday':date(1996,3,4),
                      'birth_place':'Test / City',
                      'email':'test@mail.com',
                      'phone_number':'+123456789101',
                      'address':'Top Of World'}
        self.user = create_user(self.data)
        
        self.list_url = reverse('users:api-list')
        self.retrieve_url = reverse('users:api-detail',kwargs={'pk':self.user.id})
        self.search_url = reverse('users:api-search')
        self.random_url = reverse('users:api-random')
        
        self.client = APIClient()

    def test_viewset_list_mehtod(self):
        response = self.client.get(self.list_url)
        users = UserApiModel.objects.all()
        serialized_data = UserApiSerializer(users,
                                            many=True).data
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,serialized_data)
    
    def test_viewset_retrieve_mehtod(self):
        response = self.client.get(self.retrieve_url)
        serialized_data = UserApiSerializer(instance=self.user).data
        
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,serialized_data)