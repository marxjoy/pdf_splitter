from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_upload_file_view_loads_correctly(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_no_file_selected(self):
        tester = app.test_client(self)
        response = tester.post('/',
                               data=dict(file=''),
                               follow_redirects=True)
        self.assertIn(b"No file", response.data)


    def test_bad_file(self):
        tester = app.test_client(self)
        response = tester.post('/',
                               data=dict(file='filename.txt'),
                               follow_redirects=True)
        self.assertIn(b"No file", response.data)


    def test_good_file(self):
        tester = app.test_client(self)
        response = tester.post('/',
                               data=dict(file='filename.pdf'),
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()