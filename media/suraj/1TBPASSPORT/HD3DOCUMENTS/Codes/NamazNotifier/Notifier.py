import Configure
filename = Configure.filename
filepath = Configure.filepath
def readLinkFromFile():
    url = Configure.readFromFile(filepath,filename)
    print (url)
    responseDict = Configure.getUrlResponse(url)
    print(responseDict)

def flowControl():
    readLinkFromFile()

flowControl()
