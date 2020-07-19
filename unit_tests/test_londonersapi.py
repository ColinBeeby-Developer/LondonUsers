'''
This class contains tests for LondonersApi
'''
import unittest
import json
from mock import patch
from londonersapi import Londoners


class TestLondonersApi(unittest.TestCase):
    
    USERS_LIVING_IN_CITY = '[{"id": 135,"first_name": "Mechelle","last_name": "Boam","email": "mboam3q@thetimes.co.uk","ip_address": "113.71.242.187","latitude": -6.5115909,"longitude": 105.652983}]'
    USERS_LIVING_NEAR_LOCATION = '[{"id": 688,"first_name": "Tiffi","last_name": "Colbertson","email": "tcolbertsonj3@vimeo.com","ip_address": "141.49.93.0","latitude": 37.13,"longitude": -84.08}]'

    def setUp(self):
        self._population = []

    @patch('QueryBpdtsTestApp.populationinformation.PopulationInformation.getUsersLivingInCity')
    @patch('QueryBpdtsTestApp.populationinformation.PopulationInformation.getUsersLivingNearLocation')
    def testLondonersGet(self, mockGetUsersLivingNearLocation, mockGetUsersLivingInCity):
        '''
        Test the Londoners.get method, check the response matches expected
        '''
        mockGetUsersLivingInCity.side_effect = self._getUsersLivingInCity
        mockGetUsersLivingNearLocation.side_effect = self._getUsersLivingNearLocation
        
        expectedResult = json.loads(self.USERS_LIVING_IN_CITY)
        expectedResult.extend(json.loads(self.USERS_LIVING_NEAR_LOCATION))
       
        ldnApi = Londoners()
        actualResult = ldnApi.get()
        self.assertEqual(expectedResult,
                          actualResult,
                          'Expected result and actual result do not match')

    def _getUsersLivingInCity(self,
                              _): 
        return json.loads(self.USERS_LIVING_IN_CITY)
        
    def _getUsersLivingNearLocation(self,
                                    _,
                                    __,
                                    ___):
        return json.loads(self.USERS_LIVING_NEAR_LOCATION)
      

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLondonersGet']
    unittest.main()