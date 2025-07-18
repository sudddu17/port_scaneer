# port_scanner.py

import socket

def scan_ports(target, ports):
    print(f"\nScanning {target}...\n")
    open_ports = []

    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
            sock.close()
        except:
            pass
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"\nTotal open ports: {len(open_ports)}")

def main():
    print("🔐 Website Port & Service Scanner 🔍")
    target = input("Enter website or IP (e.g. google.com or 8.8.8.8): ").strip()

    # Common ports (You can add more if you want)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

    scan_ports(target, common_ports)

if __name__ == "__main__":
    main()
