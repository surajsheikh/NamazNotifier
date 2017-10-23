from Configure import filename,filepath,readFromFile,getUrlResponse,getCurrentTimestamp
if __name__ == '__main__':
    print('calling')

def readLinkFromFile():
    url = readFromFile(filepath,filename)
    print (url)
    responseDict = getUrlResponse(url)
    print(responseDict)

def flowControl():
    readLinkFromFile()

flowControl()

