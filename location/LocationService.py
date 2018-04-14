from url.UrlService import UrlServiceClass
from termcolor import colored, cprint

#Logging related configuration
import logging
from logging.config import fileConfig
fileConfig("../config/logger.conf")
log = logging.getLogger(__name__)


class LocationServiceClass:

    def traceLocation():
        """Detects User location or asks for manually entering users location information
            1. Auto detects the locations
            2. Detects the user defined location and prints the details

            :return tuple: returns latitude, longitude, timezone
        """
        log.debug("--------Entering Method----------")
        urlTrace = 'http://freegeoip.net/json'
        responseDict = UrlServiceClass.getUrlResponse(urlTrace)
        log.debug("Response from web service")

        #Reading required information from the response json
        latitude = responseDict['latitude']
        longitude = responseDict['longitude']
        timezone = responseDict['time_zone']

        #Displaying the information to the user for confirmation
        print('Detected your city as {}, in {}, {}'.format(responseDict['city'],responseDict['region_name'],responseDict['country_name']))
        print('Latitude ', latitude, ' Longitude ',longitude, ' timezone ',timezone)
        manualchoice = input('Do you want to enter manually [Y/y/N/n]? ')

        #If user wants to enter the location information manually
        if manualchoice=='n' or manualchoice=='N' or manualchoice=='':
            cprint('Continuing with the current city','yellow')
        elif manualchoice=='Y' or manualchoice=='y':
            #while loop used to give user a choice to correct his search query
            gotoFlag = True
            while gotoFlag:
                city=input('Enter your Area, City, Country/State/Region: ')
                country='x' #input('Enter your Country: ') #Not entering country as it doesnt return the correct lat long

                #Reading the lat long information from response and default country as X (Do not change this)
                url = 'http://api.aladhan.com/cityInfo?city='+city+'&country='+country
                responseDict = UrlServiceClass.getUrlResponse(url)

                #loading the subdictionary from response
                responseDict = responseDict['data']
                latitude = responseDict['latitude']
                longitude = responseDict['longitude']
                timezone = responseDict['timezone']

                #Getting additional information from google maps for the lat long
                apiKey='AIzaSyAXFc-5WXzlHj191N9GOZ_sqGtJkON4QxE'
                url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(latitude)+','+str(longitude)+'&key='+apiKey
                print('\nTracing location based on your input....')
                responseDict = UrlServiceClass.getUrlResponse(url)

                # Based on the Array size the information will be displayed
                arraysize=len(responseDict['results'][0]['address_components'])
                locationDetails=''
                for i in range(0,arraysize):
                    locationDetails += responseDict['results'][0]['address_components'][i]['long_name']+" "
                cprint('Based on the City Code the result is {}'.format(locationDetails),'green')

                #Block to check if user wants to input again
                choice = input('\nDo you want to search again ? [y/n]: ')
                if choice.lower()=='n':
                    gotoFlag=False
                    break
                elif choice.lower()=='y':
                    continue
                else:

                    cprint('Invalid Choice, try again', 'red')
                    continue

            else:
                print('Invalid Input, Exiting!!')
                exit(10)
                print('Latitude ', latitude, ' Longitude ',longitude, ' timezone ',timezone)
                return (latitude,longitude,timezone)


        log.debug("--------Exiting Method-----------")



def main():
    LocationServiceClass.traceLocation()

if __name__ == '__main__':
    main()
