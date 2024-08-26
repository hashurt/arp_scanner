from scapy.all import ARP, Ether, srp

def arp_scan(ip_range):
    """
    Perform an ARP scan on the specified IP range.
    
    Parameters:
        ip_range (str): The IP range to scan, e.g., "192.168.1.1/24".
    
    Returns:
        list: A list of dictionaries containing IP and MAC addresses of detected devices.
    """
    # Create an ARP request packet targeting the given IP range
    arp = ARP(pdst=ip_range)
    # Create an Ethernet frame to encapsulate the ARP request
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Stack the Ethernet frame and ARP request together
    packet = ether/arp
    
    # Send the packet and receive the responses
    # srp function sends packets at layer 2 and returns a tuple of sent and received packets
    result = srp(packet, timeout=3, verbose=False)[0]
    
    # List to store discovered devices
    devices = []
    for sent, received in result:
        # Append the IP and MAC address of each discovered device to the list
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def print_result(devices):
    """
    Print the result of the ARP scan in a readable format.
    
    Parameters:
        devices (list): A list of dictionaries containing IP and MAC addresses of detected devices.
    """
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    # Define the IP range to scan (e.g., "192.168.1.1/24")
    ip_range = "192.168.1.1/24"
    
    # Perform the ARP scan
    devices = arp_scan(ip_range)
    
    # Print the scan results
    print_result(devices)
