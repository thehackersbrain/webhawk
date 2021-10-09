#!/usr/bin/env python

import requests
import json


def crtsh(domain):
    host = "https://crt.sh/?q="
    req_url = host+domain+"&output=json"
    req = requests.get(req_url)
    found_data = req.text
    data_dict = json.loads(found_data)
    subdomains = []
    for i in data_dict:
        if (i['common_name'] not in subdomains):
            subdomains.append(i['common_name'])
    return subdomains
