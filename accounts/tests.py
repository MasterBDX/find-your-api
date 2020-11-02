from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import UserProfile

User = get_user_model()


class UserTest(TestCase):
	def setUp(self):
		self.username = 'Masterbdx'
		self.user = User.objects.create(username=self.username)

	def test_user_slug(self):
		username = self.username.lower()
		self.assertIsNotNone(self.user.slug)
		self.assertIn(username,self.user.slug)




class UserProfileTest(TestCase):
	def setUp(self):
		self.username = 'Masterbdx'
		self.user = User.objects.create(username=self.username)


	def test_user_profile_creater(self):
		profile = UserProfile.objects.filter(user=self.user)
		self.assertTrue(profile.exists())
		self.assertEqual(profile.first().user.username,self.username)




