import requests
def responseValidation(requests, url):
    """Validates the response of the url
        Conditions: If response is 200 OK, continue, else exit(0)
    """
    if requests.status_code!=200:
        print('Remote host returned status:',requests.status_code, requests.reason, '''\nPlease check http://www.google.co.in/search?q=http+{}'''.format(str(requests.status_code)))
        exit(0)


def locationTracer():
    """Detects User location or asks for manually entering users location information
        1. Auto detects the locations
        2. Detects the user defined location and prints the details

        :return tuple: returns latitude, longitude, timezone
    """
    import os
    #Cleaning the OS screen
    os.system('clear')

    # Below url returns the location of the user based on the ip address
    url = 'http://freegeoip.net/json'
    responseDict = getUrlResponse(url)

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
        print('Continuing with the current city')
    elif manualchoice=='Y' or manualchoice=='y':
        city=input('Enter your Area, City, Country/State/Region: ')
        country='x' #input('Enter your Country: ') #Not entering country as it doesnt return the correct lat long

        #Reading the lat long information from response and default country as X (Do not change this)
        url = 'http://api.aladhan.com/cityInfo?city='+city+'&country='+country
        responseDict = getUrlResponse(url)

        #loading the subdictionary from response
        responseDict = responseDict['data']
        latitude = responseDict['latitude']
        longitude = responseDict['longitude']
        timezone = responseDict['timezone']

        #Getting additional information from google maps for the lat long
        apiKey='AIzaSyAXFc-5WXzlHj191N9GOZ_sqGtJkON4QxE'
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(latitude)+','+str(longitude)+'&key='+apiKey
        print('\nTracing your input details from google maps...')
        responseDict = getUrlResponse(url)

        # Based on the Array size the information will be displayed
        arraysize=len(responseDict['results'][0]['address_components'])
        locationDetails=''
        for i in range(0,arraysize):
            locationDetails += responseDict['results'][0]['address_components'][i]['long_name']+" "
        print('Based on the City Code the result is {}'.format(locationDetails))
    else:
        print('Invalid Input, Exiting!!')
        exit(10)
    print('Latitude ', latitude, ' Longitude ',longitude, ' timezone ',timezone)
    return (latitude,longitude,timezone)


def getCurrentTimestamp(timezone):
    """Returns the current Unix time for a particular timezone
        :param arg1: timezone information of the location eg: asia/kolkata
        :type arg1: string
        :returns arg1: current unix timestamp
        :rtype: int
    """
    url='http://api.aladhan.com/currentTimestamp?zone='+timezone
    responseDict = getUrlResponse(url)
    timestamp = responseDict['data']
    return(timestamp)


def getUrlResponse(url):
    """Returns the json text of from the url response after validation of http response code
        :param arg1: url string for the webservice
        :type arg1: string
        :returns arg1: json object
        :rtype: object
    """
    import json
    response = requests.get(url)
    responseValidation(response,url)
    responseDict = json.loads(response.text)
    return responseDict

def displayCalculationMethod():
    """Display the calculation method
            no args
            returns choice int"""
    print('''\n[Mandatory] These are the different methods identifying various schools of thought about how to compute the timings.
            0 - Shia Ithna-Ashari
            1 - University of Islamic Sciences, Karachi
            2 - Islamic Society of North America (ISNA)
            3 - Muslim World League (MWL)
            4 - Umm al-Qura, Makkah
            5 - Egyptian General Authority of Survey
            7 - Institute of Geophysics, University of Tehran''')
    choice = input('Enter you choice: ')
    return choice

def displaySchool():
    """Display the school option
         no args
         returns choice int"""
    print('''\n[Optional] School - If you leave this empty, it defaults to Shafii.
            0 - Shafii
            1 - Hanfi.''')
    choice = input('Enter you choice: ')
    return choice


def displayLatitudeAdjustmentMethod():
    """Display the calculation method
        no args
        returns choice int"""
    print('''\n[Optional] Method for adjusting times higher latitudes - for instance, if you are checking timings in the UK or Sweden. Defaults to 3 - Angle Based
            1 - Middle of the Night
            2 - One Seventh
            3 - Angle Based''')
    choice = input('Enter you choice: ')
    return choice

lat_lon_tz = locationTracer()
latitude = lat_lon_tz[0]
longitude = lat_lon_tz[1]
timezone = lat_lon_tz[2]
currentTimestamp = getCurrentTimestamp(timezone)
#Forming url to retrieve the timings based on location and timestamp
method = displayCalculationMethod()
school = displaySchool()
angle = displayLatitudeAdjustmentMethod()
url = 'http://api.aladhan.com/timings/'+str(currentTimestamp)+'?latitude='+str(latitude)+'&longitude='+str(longitude)+'&timezonestring='+str(timezone)+'&method='+str(method)+'&school='+str(school)+'&angle='+str(angle)
responseDict = getUrlResponse(url)
print(responseDict)


