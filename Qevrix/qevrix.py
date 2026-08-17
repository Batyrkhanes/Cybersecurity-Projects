from pyfiglet import Figlet
from modules.network import netdisc
from modules.web import web
import argparse
from modules.setup import setup

f = Figlet(font='slant')
print(f.renderText('Qevrix 1.0'))
print("="*50)
print("GitHub: https://github.com/Batyrkhanes")
print("="*50)
print()

def main():

    parser = argparse.ArgumentParser(
        prog="qevrix",
        description="Qevrix Security Toolkit"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # Network Discovery
    subparsers.add_parser(
        "network",
        help="Discover devices on the local network"
    )

    # Web Scanner
    web_parser = subparsers.add_parser(
        "web",
        help="Scan a web application for vulnerabilities"
    )

    web_parser.add_argument(
        "-u", "--url",
        required=True,
        help="Target URL"
    )
    web_parser.add_argument(
        "-w", "--wordlist",
        required=True,
        help="Path to the wordlist"
    )

    subparsers.add_parser(
    "setup",
    help="Check and setup dependencies"
)
    args = parser.parse_args()

    if args.command == "network":
        netdisc()
    elif args.command == "setup":
        setup()

    elif args.command == "web":
        web(args.url, args.wordlist)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
