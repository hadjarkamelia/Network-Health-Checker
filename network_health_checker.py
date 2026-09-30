import os
import platform

def ping_host(host):
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")

    if response == 0:
        return "UP"
    else:
        return "DOWN"


hosts = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]

print("===== NETWORK HEALTH REPORT =====")

for host in hosts:
    status = ping_host(host)
    print(f"{host} : {status}")
``
