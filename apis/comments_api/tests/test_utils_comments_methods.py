from django.test import TestCase

from apis.models import (UserApiModel,
                         PostApiModel,
                         CommentApiModel)

from apis.posts_api.utils import create_api_posts

from ..utils import create_api_comments

from datetime import date

    
class TestMethods(TestCase):
    ''' Test Utils File Function '''
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
        self.create_posts = create_api_posts(num=2)
    
    def test_comments_creator_method(self):
        ''' 
            Test create_api_comments function 
            in comments api module utils file 
        '''
        is_created = create_api_comments(num=2)
        comments_num = CommentApiModel.objects.count()
        self.assertEqual(comments_num,12)
        self.assertTrue(is_created)
        