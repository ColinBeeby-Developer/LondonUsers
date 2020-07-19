'''
This file contains classes and methods to expose the Londoners API
'''
from __future__ import print_function

from QueryBpdtsTestApp.populationinformation import PopulationInformation
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app,
          title='Londoners',
          description='An API to list users in and around London')


@api.route('/users/london')
class Londoners(Resource):
    '''
    Class exposes the /users/london endpoint
    '''
    
    def get(self):
        '''
        List users living in London or within 50 miles of London
        '''
        users = []
        populationInformation = PopulationInformation()
        users.extend(populationInformation.getUsersLivingInCity('London'))
        # longitude and latitude for Trafalgar Square
        users.extend(populationInformation.getUsersLivingNearLocation(-0.127774,
                                                          51.507886,
                                                          50))
            
        # remove any duplicate entries
        return list({user['id']:user for user in users}.values())


if __name__ == '__main__':
    app.run(port=5000)
