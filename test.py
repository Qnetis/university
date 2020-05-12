from django.test import Client, TestCase
class ViewTest(TestCase):

    def test_hello(self):
        c = Client()
        resp = c.get('/app/hello/')
        self.assertEqual(resp.status_code, 200)
