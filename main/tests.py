from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        #response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Timothée Girard')
