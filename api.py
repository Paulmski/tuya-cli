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
import variables


class API:


        


    baseurl = 'https://openapi.tuyaus.com'


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

        if variables.tuya_token == '' or int(t) - int(variables.tuya_token_timestamp) > 70000:
            headers = {'client_id': variables.tuya_id, 'sign': self.get_sign(variables.tuya_id + t, variables.tuya_secret), 'sign_method': 'HMAC-SHA256', 't': t, 'lang': 'en'}
            session = requests.Session()
            session.headers.update(headers)
            response = session.get(
                self.baseurl + '/v1.0/token?grant_type=1', headers=headers)
            print(response.text)
            result = response.json()['result']
            variables.tuya_token = result['access_token']
            variables.tuya_refresh_token = result['refresh_token']
            variables.tuya_token_timestamp = t
            print('1')
            return variables.tuya_token
        else:
            print('3')
            return variables.tuya_token


    def GET(self, url, headers={}):

        t = self.timestamp()

        default_par = {
            'client_id': variables.tuya_id,
            'access_token': self.get_tuya_token(t),
            'sign': self.get_sign(variables.tuya_id+self.get_tuya_token(t)+t, variables.tuya_secret),
            't': t,
            'sign_method': 'HMAC-SHA256',
        }
        r = requests.get(self.baseurl + url, headers=dict(default_par, **headers))

        return r


    def POST(self, url, headers={}, body={}):
        t = self.timestamp()

        default_par = {
            'client_id': variables.tuya_id,
            'access_token': self.get_tuya_token(t),
            'sign': self.get_sign(variables.tuya_id+self.get_tuya_token(t)+t, variables.tuya_secret),
            't': t,
            'sign_method': 'HMAC-SHA256',
        }
        r = requests.post(self.baseurl + url, headers=dict(default_par,
                        **headers), data=json.dumps(body))

        # Beautify the format of request result.
        r = json.dumps(r.json(), indent=2, ensure_ascii=False)
        return r    