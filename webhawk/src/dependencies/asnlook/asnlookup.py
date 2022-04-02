import requests

host = 'https://api.hackertarget.com/aslookup/?q='


def asnlookup(asnnum):
    target = host+asnnum
    req = requests.get(target)
    asndata = req.text
    return asndata
