
from api import API
class Bulb:
    __api = None
    __id = None

    def __init__(self, id, apiID, secret): 
        self.__id = id
        self.__api = API(ID=apiID, secret=secret)



    def setBrightness(self, brightness):
        command = {
        "commands": [
            {
            "code": "bright_value_v2",
            "value": brightness
        }
        ]
    }
        self.__api.POST('/v1.0/devices/' + self.__id + '/commands', body=command)




