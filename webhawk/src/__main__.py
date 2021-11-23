from rich import print
import argparse
from sys import argv
from webhawk.src.functions import basic_scan, whois, dnslookup, geoiplookup, subnetcalc, subdomains, nmapscan, builtwith, config
from webhawk import __version__


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
    elif (args.builtwith):
        scan_type('Builtwith Recon')
        builtwith(args.domain)
    else:
        scan_type('Basic Scan')
        basic_scan(args.domain)


if __name__ == "__main__":
    main()
