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


def hackertarget(domain):
    url = 'https://api.hackertarget.com/hostsearch/?q={}'.format(domain)
    req = requests.get(url)
    data = req.text.splitlines()
    subdomains = []
    for i in data:
        if (i.split(',')[0] not in subdomains):
            subdomains.append(i.split(',')[0])
    return subdomains


def subfinder(domain):
    crtsh_domains = crtsh(domain)
    hackertarget_domains = hackertarget(domain)
    found_data = crtsh_domains+hackertarget_domains
    subdomains = []
    for i in found_data:
        if (i not in subdomains):
            subdomains.append(i)

    return subdomains
