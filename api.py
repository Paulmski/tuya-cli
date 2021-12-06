import datetime
import requests
import math
from Crypto.Hash import HMAC, SHA256
import hashlib
import time
import json
import random
import sys
import colorsys


class API:

     


    BASEURL = 'https://openapi.tuyaus.com'
    __secret = None
    __ID = None
    __token = ''
    __timeStamp = ''

    @staticmethod 
    def timestamp():
        t = str(int(time.time()*1000))
        print(t)
        return t



    # https://developer.tuya.com/en/docs/iot/singnature?id=Ka43a5mtx1gsc


    def get_sign(self, msg, key):

        sign = HMAC.new(key=bytes(key, 'latin-1'), msg=bytes(msg,
                        'latin-1'), digestmod=SHA256).hexdigest().upper()
        return sign


    def get_tuya_token(self, t):

        if self.__token == '' or int(t) - int(self.__timeStamp) > 70000:
            headers = {'client_id': self.__ID, 'sign': self.get_sign(self.__ID + t, self.__secret), 'sign_method': 'HMAC-SHA256', 't': t, 'lang': 'en'}
            session = requests.Session()
            session.headers.update(headers)
            response = session.get(
                self.baseurl + '/v1.0/token?grant_type=1', headers=headers)
            print(response.text)
            result = response.json()['result']
            self.__token = result['access_token']
            variables.tuya_refresh_token = result['refresh_token']
            self.__timeStamp = t
            print('1')
            return self.__token
        else:
            print('3')
            return self.__token


    def GET(self, url, headers={}):

        t = self.timestamp()

        default_par = {
            'client_id': self.__ID,
            'access_token': self.get_tuya_token(t),
            'sign': self.get_sign(self.__ID+self.get_tuya_token(t)+t, self.__secret),
            't': t,
            'sign_method': 'HMAC-SHA256',
        }
        r = requests.get(self.baseurl + url, headers=dict(default_par, **headers))

        return r


    def POST(self, url, headers={}, body={}):
        t = self.timestamp()

        default_par = {
            'client_id': self.__ID,
            'access_token': self.get_tuya_token(t),
            'sign': self.get_sign(self.__ID+self.get_tuya_token(t)+t, self.__secret),
            't': t,
            'sign_method': 'HMAC-SHA256',
        }
        r = requests.post(self.baseurl + url, headers=dict(default_par,
                        **headers), data=json.dumps(body))

        # Beautify the format of request result.
        r = json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r