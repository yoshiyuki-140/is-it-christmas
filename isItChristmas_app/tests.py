from django.test import TestCase

# Create your tests here.


class TopPageTest(TestCase):

    def test_should_return_httpStatusCode200(self):
        '''
        トップページが存在するか否か
        単体テスト
        '''
        status_code = 200
        response = self.client.get('')
        self.assertEqual(status_code, response.status_code)
