from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import *


# Create your tests here
class TesNewsUrls(SimpleTestCase):
    def test_create_url_is_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func.__name__, PostCreateView.as_view().__name__)

    def test_blogs_url_is_resolved(self):
        url = reverse('blogs', args=['technology'])
        self.assertEquals(resolve(url).func, blogs)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)