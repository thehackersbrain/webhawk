#!/usr/bin/env python

from rich import print
import argparse
from webhawk.src.functions import basic_scan, whois, dnslookup, geoiplookup, subnetcalc, subdomains, nmapscan


def banner():
    print("[bold green]░█████   ███   █████          █████     █████   █████                           █████     [/bold green]")
    print("[bold green]░░███   ░███  ░░███          ░░███     ░░███   ░░███                           ░░███      [/bold green]")
    print("[bold green] ░███   ░███   ░███   ██████  ░███████  ░███    ░███   ██████   █████ ███ █████ ░███ █████[/bold green]")
    print("[bold green] ░███   ░███   ░███  ███░░███ ░███░░███ ░███████████  ░░░░░███ ░░███ ░███░░███  ░███░░███ [/bold green]")
    print("[bold green] ░░███  █████  ███  ░███████  ░███ ░███ ░███░░░░░███   ███████  ░███ ░███ ░███  ░██████░  [/bold green]")
    print("[bold green]  ░░░█████░█████░   ░███░░░   ░███ ░███ ░███    ░███  ███░░███  ░░███████████   ░███░░███ [/bold green]")
    print("[bold green]    ░░███ ░░███     ░░██████  ████████  █████   █████░░████████  ░░████░████    ████ █████[/bold green]")
    print("[bold green]     ░░░   ░░░       ░░░░░░  ░░░░░░░░  ░░░░░   ░░░░░  ░░░░░░░░    ░░░░ ░░░░    ░░░░ ░░░░░ [/bold green]")
    print(
        "\n                                    Created by [bold]Gaurav Raj[/bold]\n                                      [[bold green]TheHackersBrain[/bold green]]\n")


def menu():
    print("[bold yellow][00] Basic Recon (Site Title, IP Address, CMS, Cloudflare Detection, Robots.txt Scanner)[/bold yellow]")
    print("[bold yellow][01] Whois Lookup[/bold yellow]")
    print("[bold yellow][02] Geo-IP Lookup[/bold yellow]")
    print("[bold yellow][03] Grab Banners[/bold yellow]")
    print("[bold yellow][04] DNS Lookup[/bold yellow]")
    print("[bold yellow][05] Subnet Calculator[/bold yellow]")
    print("[bold yellow][06] NMAP Port Scan[/bold yellow]")
    print("[bold yellow][07] Subdomain Scanner[/bold yellow]")
    print("[bold yellow][08] Reverse IP Lookup & CMS Detection[/bold yellow]")
    print("[bold yellow][09] SQLi Scanner[/bold yellow]")
    print("[bold yellow][10] Bloggers View[/bold yellow]")
    print("[bold yellow][11] Wordpress Scanner[/bold yellow]")
    print("[bold yellow][12] Crawler[/bold yellow]")
    print("[bold yellow][13] MX Lookup[/bold yellow]")
    print("[bold magenta][A] Scan for Everything[/bold magenta]")
    print("[bold blue][F] Fix Modules[/bold blue]")
    print("[bold green][U] Check for Updates[/bold green]")
    print("[bold][B] Scan Another Website[/bold]")
    print("[bold red][Q] QUIT !!![/bold red]")


def scan_type(stype):
    print(" [[bold green]S[/bold green]] Scan Type: [[bold green]{}[/bold green]]\n".format(stype))


def main():
    # Parsing Arguments
    parser = argparse.ArgumentParser(
        description="WebHawk - Web Recon Framework")
    parser.add_argument(
        "-d", "--domain", help="Specify Target Domain", required=True)
    parser.add_argument(
        "-w", "--whois", help="Extract Whois Information for The Target Domain.", action="store_true")
    parser.add_argument(
        "-l", "--lookup", help="DNS Lookup for the Target Domain", action="store_true")
    parser.add_argument(
        "-g", "--geoip", help="GEO-IP Lookup on the Target's IP", action="store_true")
    parser.add_argument(
        "-n", "--subnet", help="Subnet Calculator for Target Domain's IP Address", action="store_true")
    parser.add_argument(
        "-s", "--subdomains", help="Find Available Subdomains for the Target's Domain", action="store_true")
    parser.add_argument(
        "-p", '--ports', help="Perform Nmap Scan on Target Domain's IP Address", action="store_true")
    args = parser.parse_args()
    banner()
    print(
        "                            [[bold green]+[/bold green]] Target Domain: [bold green]{}[/bold green]\n".format(args.domain))
    print(" [[bold green]*[/bold green]] [bold green]Scanning Started...[/bold green]")
    if(args.whois):
        scan_type('Whois Recon')
        whois(args.domain)
    elif(args.lookup):
        scan_type('DNS Lookup')
        dnslookup(args.domain)
    elif(args.geoip):
        scan_type('GEO-IP Lookup')
        geoiplookup(args.domain)
    elif(args.subnet):
        scan_type('Subnet Calculator')
        subnetcalc(args.domain)
    elif(args.subdomains):
        scan_type('Subdomains Finder')
        subdomains(args.domain)
    elif(args.ports):
        scan_type('NMAP Scan')
        nmapscan(args.domain)
    else:
        scan_type('Basic Scan')
        basic_scan(args.domain)


if __name__ == "__main__":
    main()
