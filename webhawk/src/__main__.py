from rich import print
import argparse
from sys import argv
from webhawk.src.functions import basic_scan, whois, dnslookup, geoiplookup, subnetcalc, subdomains, nmapscan, builtwith, config
from webhawk import __version__
import re


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


def scan_type(stype):
    print(" [[bold green]S[/bold green]] Scan Type: [[bold green]{}[/bold green]]\n".format(stype))


def validator(domain):
    if (domain.startswith('https://')):
        domain = domain[8:]
    elif (domain.startswith('http://')):
        domain = domain[7:]

    if ("/" in domain):
        domain = domain.split("/")[0]

    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    dmnregex = re.compile(regex)
    if (re.search(dmnregex, domain)):
        return domain


def main():
    if (len(argv) == 2 and argv[1] == '-v'):
        print("[bold green]Webhawk {}[/bold green]".format(__version__))
        exit(0)
    elif (len(argv) == 2 and argv[1] == '--config'):
        config()

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
    parser.add_argument(
        '-b', '--builtwith', help="Fire up a Builtwith Recon against the target domain", action="store_true")
    parser.add_argument(
        "--config", help='Configure Webhawk for API Uses', action="store_true")
    parser.add_argument("-v", "--version",
                        help="Print version of the Tool", action="store_true")
    args = parser.parse_args()
    banner()
    domain = validator(args.domain)
    print(
        "                            [[bold green]+[/bold green]] Target Domain: [bold green]{}[/bold green]\n".format(domain))
    print(" [[bold green]*[/bold green]] [bold green]Scanning Started...[/bold green]")
    if(args.whois):
        scan_type('Whois Recon')
        whois(domain)
    elif(args.lookup):
        scan_type('DNS Lookup')
        dnslookup(domain)
    elif(args.geoip):
        scan_type('GEO-IP Lookup')
        geoiplookup(domain)
    elif(args.subnet):
        scan_type('Subnet Calculator')
        subnetcalc(domain)
    elif(args.subdomains):
        scan_type('Subdomains Finder')
        subdomains(domain)
    elif(args.ports):
        scan_type('NMAP Scan')
        nmapscan(domain)
    elif (args.builtwith):
        scan_type('Builtwith Recon')
        builtwith(domain)
    else:
        scan_type('Basic Scan')
        basic_scan(domain)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(1)
    except EOFError:
        exit(1)
    except Exception as err:
        print(
            "[[bold red]-[/bold red]] Unexpected Error Encountered !!!\n\n{}".format(err))
