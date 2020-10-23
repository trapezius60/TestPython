#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests

url = 'https://notify-api.line.me/api/notify'
token = 'Ei5KLzQrNizl4HZfnQIFzKQeAZYoNYUUzcsWgSX5BWu' #myline notify token
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'ทดสอบภาษาไทย hello'
r = requests.post(url, headers=headers , data = {'message':msg})
print r.text
