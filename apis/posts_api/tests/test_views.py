from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


from apis.models import PostApiModel

from ..serializers import PostApiSerializer

from datetime import date

def create_post(data):
    return PostApiModel.objects.create(**data)

class TestPostsAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
                     'author_id':1,'author_name':'test_name',
                     'author_email':'test@mail.com','title':'Test Title',
                     'overview':'Test OverView Short Overview',
                     'content':'Test Content Long Content',
        
                     }
        self.post = create_post(self.data)

        self.list_url = reverse('posts:api-list')
        self.retrieve_url = reverse('posts_api:api-detail',kwargs={'pk':self.post.id})

    def test_viewset_list_method(self):
        for _ in range(3):
            create_post(self.data)
        posts = PostApiModel.objects.all()
        serialized_data = PostApiSerializer(posts,many=True).data
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,serialized_data)
    
    def test_viewset_create_method(self):
        response = self.client.post(self.list_url,self.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.data['author_id'],response.data.get('author_id'))

    
    def test_viewset_retrieve_method(self):        
        
        response = self.client.get(self.retrieve_url)
        serialized_object_data = PostApiSerializer(self.post).data
        self.assertEqual(response.status_code,200)
        self.assertEqual(serialized_object_data,response.data)

    def test_viewset_update_method(self):
        updated_data = {
                     'author_id':2,'author_name':'test_name_updated',
                     'author_email':'testupdated@mail.com','title':'Test Title Updated',
                     'overview':'Test Updated OverView Short Overview Updated',
                     'content':'Test Updated Content Long Content Updated',
        
                     }
        response = self.client.put(self.retrieve_url,data=updated_data)

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['author_id'],updated_data['author_id'])
        self.assertEqual(response.data['title'],updated_data['title'])
        self.assertEqual(response.data['content'],updated_data['content'])
    
    def test_viewset_destroy_method(self):
        response = self.client.delete(self.retrieve_url)

        self.assertEqual(response.status_code,200)