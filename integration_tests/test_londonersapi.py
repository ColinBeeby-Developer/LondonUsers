'''
Module contains integration tests for londoners API
'''
import unittest
import requests


class TestLondonersApi(unittest.TestCase):


    def testUsersLondon_cityLeeds(self):
        '''
        Test to ensure that 404 is returned when an unknown city is passed in
        '''
        (text, statusCode) = self._performCall('http://localhost:8000/users/leeds',
                                 'GET')
        
        self.assertRegex(text,
                         '404 Not Found',
                         'Returned text is not as expected')
        self.assertEqual(404,
                          statusCode,
                          'Returned status code is not as expected')
                          
        
    def testUsersLondon_post(self):
        '''
        Test to ensure that POSTing to the end point gives an error
        '''
        (text, statusCode) = self._performCall('http://localhost:8000/users/london',
                                 'POST')
        
        self.assertRegex(text,
                         'method is not allowed',
                         'Returned text is not as expected')
        self.assertEqual(405,
                          statusCode,
                          'Returned status code is not as expected')
        
    def _performCall(self,
                     url,
                     verb):
        '''
        Perform the curl call
        '''
        response = None
        if verb == 'GET':
            response = requests.get(url)
        elif verb == 'POST':
            response = requests.post(url)
        
        if not response.status_code:
            return ('',
                    999)
        return (response.text,
                response.status_code)
        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
