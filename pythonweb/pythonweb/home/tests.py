from django.test import TestCase,SimpleTestCase

# Create your tests here.
class SimpleTests(TestCase):
    def Test_home_page_status(self):
        response = self.client.get('/') 
        self.assertEquals(response.status_code,200)
