from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.stiri_url = reverse('stiri', args=['technology'])

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_stiri_GET(self):
        response = self.client.get(self.stiri_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stiri.html')