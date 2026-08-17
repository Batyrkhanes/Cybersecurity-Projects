import subprocess

def web(target, wordlist):
    print("=" * 20 + " Web Scanner " + "=" * 20)
    print(f"Target: {target}")
    print(f"Wordlist: {wordlist}")
    print("=" * 50)

    run_nmap(target)
    run_gobuster(target, wordlist)
    run_sqlmap(target)

    print("\n[+] Web scanning completed.")

def run_nmap(target, port_range="1-65535"):
    print("\n[+] Running Nmap...")
    command = ["nmap", "-sV", "-sC", "-p", port_range, target]
    subprocess.run(command)

def run_gobuster(target, wordlist):
    print("\n[+] Running Gobuster...")
    command = ["gobuster", "dir", "-u", target, "-w", wordlist]
    subprocess.run(command)

def run_sqlmap(target):
    print("\n[+] Running SQLMap...")
    command = ["sqlmap", "-u", target]
    subprocess.run(command)

def run_nikto(target):
    print("\n[+] Running Nikto...")
    command = ["nikto", "-h", target]
    subprocess.run(command)
