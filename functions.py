#!/usr/bin/env python

import requests
from rich import print
from bs4 import BeautifulSoup
import socket


def check_protocol(domain):
    url = 'http://{}'.format(domain)
    req = requests.get(url)
    if("https" not in req.url):
        print(
            " [[bold yellow]+[/bold yellow]] [bold cyan]Protocol[/bold cyan]: [bold green]HTTP[/bold green]")
    else:
        print(
            "[[bold yellow]+[/bold yellow]] [bold cyan]Protocol[/bold cyan]: [bold green]HTTPS[/bold green]")
    print("[[bold yellow]+[/bold yellow]] [bold cyan]Redirected URL[/bold cyan]: [bold green]{}[/bold green]".format(req.url))
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.find_all('title')
    print("[[bold yellow]+[/bold yellow]] [bold cyan]Site Title[/bold cyan]: [bold green]{}[/bold green]".format(title[0].get_text()))
    print("[[bold yellow]+[/bold yellow]] [bold cyan]IP Address[/bold cyan]: [bold green]{}[/bold green]".format(socket.gethostbyname(domain)))
    print("[[bold yellow]+[/bold yellow]] [bold cyan]Server[/bold cyan]: [bold green]{}[/bold green]".format(req.headers['Server']))
    print("[[bold yellow]+[/bold yellow]] [bold cyan]CMS[/bold cyan]: [bold red]Could Not Detect[/bold red]")
    print("[[bold yellow]+[/bold yellow]] [bold cyan]Cloudflare[/bold cyan]: [bold red]Not Detect[/bold red]")
    rreq = requests.get(url+'/robots.txt')
    if(rreq.status_code != 404):
        print("[[bold yellow]+[/bold yellow]] [bold cyan]Robots.txt[/bold cyan]: [bold green]Found[/bold green]")
