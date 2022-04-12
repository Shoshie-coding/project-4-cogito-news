from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.blogs_url = reverse('blogs', args=['technology'])
        self.post_detail_url = reverse('Post_detail', args=['seriouspost'])

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')  

    def test_blogs_GET(self):
        response = self.client.get(self.blogs_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs.html')
