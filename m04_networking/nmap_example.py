import nmap
from pprint import pprint

nm = nmap.PortScanner()

while True:

    ip = input("\nInput IP address to scan: ")
    if not ip:
        break

    print(f"\n--- beginning scan of {ip}")
    output = nm.scan(ip, '22-1024', arguments="-sS -sU -O --host-time 600")
    print(f"--- --- command: {nm.command_line()}")

    print("----- nmap scan output -------------------")
    pprint(output)

    try:
        pprint(nm[ip].all_tcp())
        pprint(nm[ip].all_udp())
        pprint(nm[ip].all_ip())
    except KeyError as e:
        print(f"   ---> failed to get scan results for {ip}")

    print(f"--- end scan of {ip}")

print("\nExiting nmap scanner")
