from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


from apis.models import UserApiModel,PostApiModel
from ..utils import (get_new_post,
                     get_serialized_data,
                     create_api_posts)

from ..serializers import PostApiSerializer

from datetime import date

def create_post(data):
    return PostApiModel.objects.create(**data)

class TestPostsAPIViews(TestCase):
    def setUp(self):
        self.list_url = reverse('posts_api:api-list')
        self.client = APIClient()
        self.data = {
                     'author_id':1,'author_name':'test_name',
                     'author_email':'test@mail.com','title':'Test Title',
                     'overview':'Test OverView Short Overview',
                     'content':'Test Content Long Content',
                     }

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
        


class TestMethods(TestCase):
    '''Test utils file method for posts API module'''

    def setUp(self):
        self.today = date.today()
        
        # This user not from Main User Model but from User Fake API Model.
        #------------------------------------------------------------------
        self.user = UserApiModel.objects.create(first_name='test',
                                        last_name='bdx',
                                        gender='male',
                                        birthday=self.today,
                                        birth_place='test place',
                                        email='test@email.com',
                                        phone_number='218931239763',
                                        address='Test Street',
                                        )
        self.data = {'title':'Test Post',
                     'overview':'test overview',
                     'content':'Test Content',
                     'author_id':self.user.id,
                     'published_at':self.today}

        self.updated_data = {'title':'Test Post Updated',
                     'overview':'test overview Updated',
                     'content':'Test Content Updated',
                     'author_id':self.user.id,
                     'published_at':self.today}

        self.post = PostApiModel.objects.create(
                                title=self.data['title'],
                                overview=self.data['overview'],
                                content=self.data['content'],
                                author_id=self.data['author_id'],
                                published_at=self.data['published_at'])

    def test_new_post_method(self):
        '''Test get_new_post method'''

        obj = get_new_post(self.data)
        self.assertEqual(obj.title,self.data['title'])
        self.assertEqual(obj.overview,self.data['overview'])
        self.assertEqual(obj.content,self.data['content'])
        self.assertEqual(obj.author_id,self.user.id)
        self.assertEqual(obj.published_at,self.today)
        self.assertTrue(type(obj.id)==int)
    
    def test_serialized_data_method(self):
        '''Test get_serialized_data_method without pass any data '''
        pk = self.post.pk
        serilaizer_data = PostApiSerializer(self.post).data
        data,status_code = get_serialized_data(pk)
        self.assertEqual(data,serilaizer_data)
        self.assertEqual(status_code,status.HTTP_200_OK)
    
    def test_serialized_data_method2(self):
        '''Test get_serialized_data_method with pass data kwarg 
            & without partial kwarg to test if fail with non full 
            data passed 
        '''
        pk = self.post.pk
        serilaizer_data = PostApiSerializer(self.post).data
        data,status_code = get_serialized_data(pk,self.updated_data)
        data2,status_code2 = get_serialized_data(pk,{'title':'Test Title 2'})
        
        self.assertEqual(self.updated_data['title'],data['title'])
        self.assertNotEqual(data,serilaizer_data)
        self.assertEqual(status_code,status.HTTP_200_OK)
        self.assertEqual(status_code2,status.HTTP_400_BAD_REQUEST)
    
    def test_serialized_data_method2(self):
        '''Test get_serialized_data_method with pass data kwarg 
            &  partial kwarg
        '''
        pk = self.post.pk
        serilaizer_data = PostApiSerializer(self.post).data
        data,status_code = get_serialized_data(pk,{'title':'Test Title 2'},partial=True)
        
        self.assertEqual('Test Title 2',data.get('title',None))
        self.assertNotEqual(data,serilaizer_data)
        self.assertEqual(status_code,status.HTTP_200_OK)
    

class TestMethods2(TestCase):
    def setUp(self):
        self.today = date.today()
        self.user = UserApiModel.objects.create(first_name='test',
                                        last_name='bdx',
                                        gender='male',
                                        birthday=self.today,
                                        birth_place='test place',
                                        email='test@email.com',
                                        phone_number='218931239763',
                                        address='Test Street')
        
        self.user2 = UserApiModel.objects.create(first_name='test2',
                                        last_name='bdx',
                                        gender='male',
                                        birthday=self.today,
                                        birth_place='test place',
                                        email='test2@email.com',
                                        phone_number='218931239763',
                                        address='Test Street')

        self.user3 = UserApiModel.objects.create(first_name='test3',
                                        last_name='bdx',
                                        gender='male',
                                        birthday=self.today,
                                        birth_place='test place',
                                        email='test3@email.com',
                                        phone_number='218931239763',
                                        address='Test Street')

    
    def test_posts_creator_method(self):
        created = create_api_posts(num=3)
        posts_num = PostApiModel.objects.count()
        self.assertEqual(posts_num,9)
        self.assertTrue(created)
