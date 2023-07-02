import netifaces

def get_lan_info():
    interfaces = netifaces.interfaces()
    lan_info = []

    for iface in interfaces:
        if iface != 'lo':  # Exclude the loopback interface
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                ip_info = addrs[netifaces.AF_INET][0]
                ip_address = ip_info['addr']
                netmask = ip_info['netmask']
                gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
                lan_info.append({
                    'interface': iface,
                    'ip_address': ip_address,
                    'netmask': netmask,
                    'gateway': gateway
                })

    return lan_info

# Usage
lan_info = get_lan_info()
for info in lan_info:
    print(f"Interface: {info['interface']}")
    print(f"IP Address: {info['ip_address']}")
    print(f"Netmask: {info['netmask']}")
    print(f"Gateway: {info['gateway']}")
    print()
