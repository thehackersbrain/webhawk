#!/usr/bin/env python

import requests
from rich import print
from bs4 import BeautifulSoup

url = ''


def check_protocol(domain):
    url = 'http://{}'.format(domain)
    req = requests.get(url)
    if("https" not in req.url):
        print(
            " [[bold yellow]+[/bold yellow]] Protocol: [[bold green]HTTP[/bold green]]")
    else:
        print(
            " [[bold yellow]+[/bold yellow]] Protocol: [[bold green]HTTPS[/bold green]]")
    print(" [[bold yellow]+[/bold yellow]] Redirected URL: [[bold green]{}[/bold green]]".format(req.url))
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.find_all('title')
    print("[[bold yellow]+[/bold yellow]] Site Title: [bold green]{}[/bold green]".format(title[0]))
