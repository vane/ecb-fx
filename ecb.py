#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime
import requests

url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?00028374c23d027b48a2f227a88071f3'
resp = requests.get(url)

dt = datetime.now()
dt_fname = dt.strftime('%Y-%m-%d')
dt_folder_name = dt.strftime('%Y')
if not os.path.exists(f'data/{dt_folder_name}'):
    os.makedirs(f'data/{dt_folder_name}')

with open(f'data/{dt_folder_name}/{dt_fname}.xml', 'wb+') as f:
    f.write(resp.content)
