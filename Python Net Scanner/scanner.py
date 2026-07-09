import socket
from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from pyfiglet import Figlet

COMMON_PORTS = [20,21,22,23,25,53,80,110,135,139,143,443,445,3306,3389,8000, 8080]
SERVICES = {22: "SSH",80: "HTTP",443: "HTTPS",53: "DNS",21: "FTP",25: "SMTP",445: "SMB",3389: "RDP"}

f = Figlet(font='slant')
print(f.renderText('Net Scanner v1.0'))
print("="*50)
print("Author: Yessengali Batyrkhan")
print("GitHub: https://github.com/Batyrkhanes")
print("Features: ARP scan, MAC vendor, hostname, and port scanning.")
print("="*50)

lookup = MacLookup()
lookup.update_vendors()

def ip_mask():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80)) #make OS choose the right interface to connect to the internet
        ip = s.getsockname()[0]
        return ip
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    finally:
        s.close()
    
def get_network(ip):
    ip_parts = '.'.join(ip.split('.')[:3]) + '.0/24'
    return ip_parts

def get_vendor(mac):
    try:
        return lookup.lookup(mac)
    except Exception as e:
        return "Unknown"

def scan_network(target):
    print()
    print("Scanning network...")
    print()
    arp = ARP(pdst=target)
    ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ethernet / arp
    result = srp(packet, timeout=3, verbose=0)[0]
    print(f"{'#':<4}{'IP Address':<18}{'MAC Address':<20}{'Vendor':<35}{'Hostname'}")
    print("-" * 90)
    for index, (sent, received) in enumerate(result, start=1):
        vendor = get_vendor(received.hwsrc)
        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except socket.herror:
            hostname = "Unknown"
        print(f"{index:<4}{received.psrc:<18}{received.hwsrc:<20}{vendor:<35}{hostname}")
    return result

def main():
    found = False
    det_range = ip_mask()
    if det_range is None:
        print("Could not determine IP address.")
    else:
        network = get_network(det_range)
        result = scan_network(network)
        try:
            choose = input("Choose an # for details (type 'exit' to quit): ").lower()
            if choose == "exit":
                print("Exiting...")
                exit()
            elif choose == "":
                main()
            else:
                choose = int(choose)
                if 1 <= choose <= len(result):
                    selected = result[choose - 1][1]
                    print(f"Details for {selected.psrc}:")
                    print(f"IP Address: {selected.psrc}")
                    print(f"MAC Address: {selected.hwsrc}")
                    print(f"Vendor: {get_vendor(selected.hwsrc)}")
                    print("Finding open ports...")
                    for port in COMMON_PORTS:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        final = sock.connect_ex((selected.psrc, port))
                        if final == 0:
                            found = True
                            service = SERVICES.get(port, "Unknown")
                            print(f"Port {port:<6} is open {service:<10}")
                        sock.close()
                    if not found:
                        print("No open ports found.")
                    enter = input("Press Enter to continue...")
                    
                    if enter == "":
                        main()
                else:
                    print("Invalid selection.")

        except KeyboardInterrupt:
            print("\nOperation cancelled.")

def menu():
    print()
    print("="*23 + " Menu " + "="*23)
    print("1. Scan Network")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        main()
    elif choice == "2":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice.")
        menu()


if __name__ == "__main__":
    menu()
