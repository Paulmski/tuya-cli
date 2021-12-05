
from api import API
class Bulb:
    api = API()
    id = None

    def __init__(self, id): 
        self.id = id



    def setBrightness(self, brightness):
        command = {
        "commands": [
            {
            "code": "bright_value_v2",
            "value": 600
        }
        ]
    }
        self.api.POST('/v1.0/devices/' + self.id + '/commands', body=command)




bulb = Bulb('eb2394ad1d39a56ea2ldru')
bulb.setBrightness(200)