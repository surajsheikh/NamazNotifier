import json
import requests

#Logging related configuration
import logging
from logging.config import fileConfig
fileConfig("../config/logger.conf")
log = logging.getLogger(__name__)

class UrlServiceClass:

    def getUrlResponse(url):
        """Returns the json text of from the url response after validation of http response code
            :param arg1: url string for the webservice
            :type arg1: string
            :returns arg1: json object
            :rtype: object
        """

        log.debug("--------Entering Method----------")
        log.debug("connecting to url: %s", url)
        try:
            response = requests.get(url)
            UrlServiceClass.responseValidation(response,url)
            responseDict = json.loads(response.text)
        except json.decoder.JSONDecodeError as Argument:
            log.error("Encountered an error while decoding to json")
            return
        log.debug("--------Exiting Method-----------")
        return responseDict


    def responseValidation(requests, url):
        """Validates the response of the url
            Conditions: If response is 200 OK, continue, else exit(0)
        """
        log.debug("--------Entering Method----------")
        if requests.status_code!=200:
            log.error("Remote host returned status:",requests.status_code, requests.reason, " Please check http://www.google.co.in/search?q=http+{} ".format(str(requests.status_code)))
            #print('Remote host returned status:',requests.status_code, requests.reason, '''\nPlease check http://www.google.co.in/search?q=http+{}'''.format(str(requests.status_code)))
            exit(0)
        log.debug("--------Exiting Method-----------")


def main():
    UrlServiceClass.getUrlResponse("http://www.aol.in")

if __name__ == '__main__':
    main()
