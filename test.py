import unittest
import app

# from app.main import *

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_hello_hello(self):
        rv = self.app.get('/tbank/')

        response = {
                        "data": "tBank API is up and running", 
                        "status": "success"
                    }

        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, response)

    # def test_hello_name(self):
    #     name = 'Kenny'
    #     rv = self.app.get(f'/tbank/{name}')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()