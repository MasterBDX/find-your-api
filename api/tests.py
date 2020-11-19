from django.test import TestCase,Client

from main.models import SiteInfo
from .context import site_name

class ContextTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.obj = SiteInfo.objects.create(title='MasterBDX')

    
    def test_context_site_name(self):
        request = self.c.get('/')
        self.assertEqual(self.obj.title,site_name(request).get('title'))