from django.test import TestCase

from ..utils import get_new_post
from apis.models import UserApiModel

from datetime import date

class TestMethods(TestCase):
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
                     'author_id':self.user,
                     'published_at':self.today}
    
    def test_new_post_method(self):
        obj = get_new_post(self.data)
        self.assertEqual(obj.title,self.data['title'])
        self.assertEqual(obj.overview,self.data['overview'])
        self.assertEqual(obj.content,self.data['content'])
        self.assertEqual(obj.author_id,self.user)
        self.assertEqual(obj.published_at,self.today)
        self.assertTrue(type(obj.id)==int)