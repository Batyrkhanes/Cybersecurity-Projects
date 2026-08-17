import shutil


TOOLS = [
    "nmap",
    "gobuster",
    "nikto",
    "sqlmap"
]


def check_tools():

    print("\n[+] Checking security tools...\n")

    for tool in TOOLS:

        if shutil.which(tool):
            print(f"[✓] {tool}")
        else:
            print(f"[✗] {tool} not found")


def setup():
    print("=" * 20 + " QEVRIX SETUP " + "=" * 20)

    check_tools()
    choice = input("\nDo you want to install missing tools? (y/n): ")
    if choice.lower() == "y":
        print() ########################
    elif choice.lower() == "n":
        print("\n[+] Setup completed.")
    else:
        print("\n[!] Invalid choice. Please enter 'y' or 'n'.")
