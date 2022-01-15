
from SmartDevice import SmartDevice
class Bulb(SmartDevice):
    pass




    # Set the brightness of a standard bulb
    # Brightness: The brightness value can be between 0-1000
    def setBrightness(self, brightness):
        command = {
        "commands": [
            {
            "code": "bright_value_v2",
            "value": brightness
        }
        ]
    }
        r = self._api.POST(url='/v1.0/devices/' + self._id + '/commands', body=command)
        return r

    def setWarmth(self, warmth):
        command = {
        "commands": [
            {
            "code": "temp_value_v2",
            "value": warmth
        }
        ]
    }
        r = self._api.POST(url='/v1.0/devices/' + self._id + '/commands', body=command)
        return r

        

    def getWarmth(self):
        return int(self.getStatus()['result'][3]['value'])
    def getBrightness(self):
        return int(self.getStatus()['result'][2]['value'])

