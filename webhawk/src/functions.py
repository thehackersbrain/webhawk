import requests
from rich import print
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from bs4 import BeautifulSoup
import socket
from webhawk.src.dependencies.subdomain.subdomains import subfinder
from webhawk.src.dependencies.cmsdetector.cmsdetector import scan
import json
import os.path


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

    try:
        server = req.headers['Server']
        print("[[bold yellow]+[/bold yellow]] [bold cyan]Server[/bold cyan]: [bold green]{}[/bold green]".format(server))
        if (server == 'cloudflare'):
            print(
                "[[bold yellow]+[/bold yellow]] [bold cyan]Cloudflare[/bold cyan]: [bold green]Detected[/bold green]")
        else:
            print(
                "[[bold yellow]+[/bold yellow]] [bold cyan]Cloudflare[/bold cyan]: [bold red]Not Detect[/bold red]")
    except Exception as err:
        print("[[bold yellow]+[/bold yellow]] [bold cyan]Server[/bold cyan]: [bold red]Not Detected[/bold red]")

    cms = scan(url)
    if (cms != None):
        print("[[bold yellow]+[/bold yellow]] [bold cyan]CMS[/bold cyan]: [bold green]{}[/bold green]".format(cms))
    else:
        print("[[bold yellow]+[/bold yellow]] [bold cyan]CMS[/bold cyan]: [bold red]Not Detected[/bold red]")
    rreq = requests.get(url+'/robots.txt')
    if(rreq.status_code != 404):
        print("[[bold yellow]+[/bold yellow]] [bold cyan]Robots.txt[/bold cyan]: [bold green]Found[/bold green]")
    print(
        "------------------------------------[ [bold green]Headers[/bold green] ]------------------------------------")
    for i in req.headers:
        print("{}: {}".format(i, req.headers[i]))
    print(
        "--------------------------------[ [bold green]End of Headers[/bold green] ]------------------------------------")


def read_json(path: str):
    fullpath = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "data/" + path)
    with open(fullpath, "rb") as myfile:
        return json.loads(myfile.read())


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


def builtwith(domain):
    config = read_json("config.json")
    url = 'https://api.builtwith.com/v19/api.json?KEY={}&LOOKUP={}'.format(
        config['builtwith-api'], domain)
    req = requests.get(url)
    data = req.json()
    technologies = data['Results'][0]['Result']['Paths'][0]['Technologies']
    print(
        "------------------------------------ [ [bold green]Builtwith Recon[/bold green] ]------------------------------------")
    sn = 0
    for i in technologies:
        print("[[bold green]+[/bold green]] {}".format(technologies[sn]['Name']))
        sn += 1
    print(
        "------------------------------------ [ [bold green]Builtwith Recon[/bold green] ]------------------------------------")


def config():
    banner = Text("Webhawk Configuration Wizard",
                  justify='center', style='green bold underline')
    print(Panel(banner))
    print()
    print("1. Builtwith API\n")
    opt = input("> Choose Option: ")
    builtwith_api = Prompt.ask("[bold green]Enter API Key[/bold green]")
    if (int(opt) == 1):
        fullpath = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "data/config.json")
        with open(fullpath, 'r+') as config_file:
            data = json.load(config_file)
            data['builtwith-api'] = builtwith_api
            config_file.seek(0)
            json.dump(data, config_file, indent=4)
            config_file.truncate()
        exit()
    else:
        print("[bold red]Enter Valid Option[/bold red]")
        exit(1)
