import subprocess
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor, as_completed


def web(target, wordlist):
    print("=" * 20 + " Web Scanner " + "=" * 20)
    print("Phases: Nmap -> Gobuster -> Nikto -> SQLMap")
    print("Please wait few minutes...")
    targets = parse_target(target)
    host = targets["host"]
    base_url = targets["base_url"]
    original = targets["original"]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(run_nmap, host): "Nmap",
            executor.submit(run_gobuster, base_url, wordlist): "Gobuster",
            executor.submit(run_nikto, base_url): "Nikto",
        }

        for future in as_completed(futures):
            name = futures[future]

            try:
                result = future.result()

                print("\n\n" + "=" * 15 + f" {name} " + "=" * 15)
                print(result)

            except Exception as e:
                print(f"\n[!] {name} failed: {e}")
    if has_parameters(original):
        print("[+] Parameters found. Launching SQLMap...")
        print("\n\n" + "=" * 15 + "SQLMap" + "=" * 15)
        run_sqlmap(original)
    else:
        print("[-] No parameters found, skipping SQLMap")
    print("\n[+] Web scanning completed.")


def run_nmap(host, port_range="1-65535"):

    command = [
        "nmap",
        "-sV",
        "-sC",
        "-p",
        port_range,
        host
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    useful_lines = []

    for line in result.stdout.splitlines():
        line = line.strip()

        if (
            "/tcp" in line
            or "/udp" in line
            or line.startswith("Nmap scan report")
            or line.startswith("Host is up")
        ):
            useful_lines.append(line)

    return "\n".join(useful_lines)


def run_gobuster(target, wordlist):
    command = [
        "gobuster",
        "dir",
        "-u",
        target,
        "-w",
        wordlist
    ]
    subprocess.run(command)


def run_nikto(target):
    command = [
        "nikto",
        "-h",
        target
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    useful_lines = []

    for line in result.stdout.splitlines():
        line = line.strip()

        if line.startswith("+ "):
            useful_lines.append(line)

    return "\n".join(useful_lines)


def run_sqlmap(target):
    command = [
        "sqlmap",
        "-u",
        target
    ]

    subprocess.run(command)

def has_parameters(target):
    parsed = urlparse(target)
    parameters = parse_qs(parsed.query)
    return bool(parameters)

def parse_target(target):
    #original target: http://....?id=1
    #host: ...
    #base_url: http://...
    parsed = urlparse(target)
    host = parsed.hostname
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    return {
        "original": target,
        "host": host,
        "base_url": base_url
    }
