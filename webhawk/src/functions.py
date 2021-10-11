#!/usr/bin/env python

import requests
from rich import print
from bs4 import BeautifulSoup
import socket
from webhawk.src.dependencies.subdomain.subdomains import subfinder


def basic_scan(domain):
    url = 'http://{}'.format(domain)
    req = requests.get(url)
    if("https" not in req.url):
        print(
            "[[bold yellow]+[/bold yellow]] [bold cyan]Protocol[/bold cyan]: [bold green]HTTP[/bold green]")
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
    if (req.headers['Server'] == 'cloudflare'):
        print("[[bold yellow]+[/bold yellow]] [bold cyan]Cloudflare[/bold cyan]: [bold green]Detected[/bold green]")
    else:
        print("[[bold yellow]+[/bold yellow]] [bold cyan]Cloudflare[/bold cyan]: [bold red]Not Detect[/bold red]")
    rreq = requests.get(url+'/robots.txt')
    if(rreq.status_code != 404):
        print("[[bold yellow]+[/bold yellow]] [bold cyan]Robots.txt[/bold cyan]: [bold green]Found[/bold green]")
    print(
        "------------------------------------[ [bold green]Headers[/bold green] ]------------------------------------")
    for i in req.headers:
        print("{}: {}".format(i, req.headers[i]))
    print(
        "--------------------------------[ [bold green]End of Headers[/bold green] ]------------------------------------")


def whois(domain):
    url = "https://www.whois.com/whois/{}".format(domain)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    data = soup.find('pre', {'id': 'registryData'})
    print(
        "------------------------------------[ [bold green]Whois Information[/bold green] ]------------------------------------")
    print(data.get_text())
    print(
        "---------------------------------[ [bold green]End of the Information[/bold green] ]------------------------------------")


def dnslookup(domain):
    url = 'https://api.hackertarget.com/dnslookup/?q={}'.format(domain)
    req = requests.get(url)
    print(
        "------------------------------------[ [bold green]DNS Lookup[/bold green] ]------------------------------------")
    print(req.text)
    print(
        "--------------------------------[ [bold green]DNS Lookup Ends Here[/bold green] ]------------------------------------")


def geoiplookup(domain):
    ip = socket.gethostbyname(domain)
    url = 'https://api.hackertarget.com/geoip/?q={}'.format(ip)
    req = requests.get(url)
    print(
        "------------------------------------[ [bold green]GEO-IP Lookup[/bold green] ]------------------------------------")
    print(req.text)
    print(
        "--------------------------------[ [bold green]GEO-IP Lookup Ends Here[/bold green] ]------------------------------------")


def subnetcalc(domain):
    ip = socket.gethostbyname(domain)
    url = 'https://api.hackertarget.com/subnetcalc/?q={}'.format(ip)
    req = requests.get(url)
    print(
        "------------------------------------[ [bold green]Subnet Calculator[/bold green] ]------------------------------------")
    print(req.text)
    print(
        "------------------------------------[ [bold green]Content Ends Here[/bold green] ]------------------------------------")


def subdomains(domain):
    subdomains = subfinder(domain)
    print(
        "------------------------------------[ [bold green]Subdomain Finder[/bold green] ]------------------------------------")
    for i in subdomains:
        print("[[bold green]+[/bold green]] {}".format(i))
    print(
        "------------------------------------[ [bold green]Subdomain Finder[/bold green] ]------------------------------------")


def nmapscan(domain):
    url = 'https://api.hackertarget.com/nmap/?q={}'.format(
        socket.gethostbyname(domain))
    req = requests.get(url)
    print(
        "------------------------------------[ [bold green]NMAP Scan[/bold green] ]------------------------------------")
    print(req.text)
    print(
        "--------------------------------[ [bold green]NMAP Scan Ends Here[/bold green] ]------------------------------------")
