'''
Unit tests for the PopulationInformation class
'''
import unittest
from QueryBpdtsTestApp.populationinformation import PopulationInformation

class TestPopulationInformation(unittest.TestCase):
    '''
    Class contains unit tests for PopulationInformation class
    '''
    
    LONDON_USERS = [{'id': 135, 'first_name': 'Mechelle', 'last_name': 'Boam', 'email': 'mboam3q@thetimes.co.uk', 'ip_address': '113.71.242.187', 'latitude': -6.5115909, 'longitude': 105.652983}, {'id': 396, 'first_name': 'Terry', 'last_name': 'Stowgill', 'email': 'tstowgillaz@webeden.co.uk', 'ip_address': '143.190.50.240', 'latitude': -6.7098551, 'longitude': 111.3479498}, {'id': 520, 'first_name': 'Andrew', 'last_name': 'Seabrocke', 'email': 'aseabrockeef@indiegogo.com', 'ip_address': '28.146.197.176', 'latitude': '27.69417', 'longitude': '109.73583'}, {'id': 658, 'first_name': 'Stephen', 'last_name': 'Mapstone', 'email': 'smapstonei9@bandcamp.com', 'ip_address': '187.79.141.124', 'latitude': -8.1844859, 'longitude': 113.6680747}, {'id': 688, 'first_name': 'Tiffi', 'last_name': 'Colbertson', 'email': 'tcolbertsonj3@vimeo.com', 'ip_address': '141.49.93.0', 'latitude': 37.13, 'longitude': -84.08}, {'id': 794, 'first_name': 'Katee', 'last_name': 'Gopsall', 'email': 'kgopsallm1@cam.ac.uk', 'ip_address': '203.138.133.164', 'latitude': 5.7204203, 'longitude': 10.901604}]
    NEAR_LOCATION_USERS = [{'id': 266, 'first_name': 'Ancell', 'last_name': 'Garnsworthy', 'email': 'agarnsworthy7d@seattletimes.com', 'ip_address': '67.4.69.137', 'latitude': 51.6553959, 'longitude': 0.0572553}, {'id': 322, 'first_name': 'Hugo', 'last_name': 'Lynd', 'email': 'hlynd8x@merriam-webster.com', 'ip_address': '109.0.153.166', 'latitude': 51.6710832, 'longitude': 0.8078532}, {'id': 554, 'first_name': 'Phyllys', 'last_name': 'Hebbs', 'email': 'phebbsfd@umn.edu', 'ip_address': '100.89.186.13', 'latitude': 51.5489435, 'longitude': 0.3860497}]
    LONDON_LONGITUDE = -0.127774
    LONDON_LATITUDE = 51.507886
    WITHIN_MILES = 50
    
    def testGetUsersLivingInCity(self):
        '''
        Test that the getUsersLivingInCity method returns the expected result
        '''
        expectedUsersInCity = self.LONDON_USERS
        populationInformation = PopulationInformation()
        actualUsersInCity = populationInformation.getUsersLivingInCity('London')
        self.assertEqual(expectedUsersInCity,
                         actualUsersInCity,
                         'Expected and actual users in city do not match')
   
    def testGetUsersLivingNearLocation(self):
        '''
        Test that the getUsersLivingNearLocation method returns the expected result
        '''
        expectedUsersNearLocation = self.NEAR_LOCATION_USERS
        
        populationInformation = PopulationInformation()
        actualUsersNearLocation = populationInformation.getUsersLivingNearLocation(self.LONDON_LONGITUDE,
                                                                                   self.LONDON_LATITUDE,
                                                                                   self.WITHIN_MILES)
        
        self.assertEqual(expectedUsersNearLocation,
                         actualUsersNearLocation,
                         'Expected and actual users near location do not match')
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()