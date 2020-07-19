'''
Contains classes and methods to gather population information for bpdts-test-app
'''
import json
import requests
from geopy.distance import geodesic
from io import BytesIO

 
class PopulationInformation(object):
    '''
    A class to implement an API which exposes methods to acquire user data
    '''

    def __init__(self,
                 baseUrl='https://bpdts-test-app.herokuapp.com'):
        '''
        Constructor
        '''
        self._baseUrl = baseUrl
        
    def getUsersLivingInCity(self,
                               city):
        '''
        Return a list of user who are living in the specified city
        '''
        users = self._makeApiCall('{}/city/{}/users'.format(self._baseUrl, 
                                                            city))
        return json.loads(users)
                
                
    def getUsersLivingNearLocation(self,
                                    longitude,
                                    latitude,
                                    miles):
        '''
        Identify users living 'miles' of location specified by longitude and latitude
        '''
        givenLocation = (latitude,
                         longitude)
        
        allUsers = self._makeApiCall('{}/users'.format(self._baseUrl))
        allUsersJson = json.loads(allUsers)
        
        usersNearLocation = []
        for user in allUsersJson:
            userLocation = (float(user.get('latitude',
                                           0.0)),
                            float(user.get('longitude',
                                           0.0)))
            distance = geodesic(givenLocation,
                                userLocation).miles
            if distance <= miles:
                usersNearLocation.append(user)
                
        return usersNearLocation

    
    def _makeApiCall(self,
                     url):
        '''
        Make the call to the API and return the result
        ''' 
        response = requests.get(url)
      
        return response.text
