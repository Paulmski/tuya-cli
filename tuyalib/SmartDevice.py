from requests import get



class SmartDevice:
    def __init__(self, id, api): 
        self._id = id
        self._api = api

    def getStatus(self):
        return self._api.GET("/v1.0/iot-03/devices/{}/status".format(self._id)).json()


    def getFunctions(self):
        return self._api.GET("/v1.0/iot-03/devices/{}/functions".format(self._id)).json()
