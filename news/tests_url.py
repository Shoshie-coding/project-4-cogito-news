from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import *


# Create your tests here
class TestMenusUrls(SimpleTestCase):
    def test_create_url_is_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func, PostCreateView.as_view())

