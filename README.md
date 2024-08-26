ARP Scanner
This is a simple ARP (Address Resolution Protocol) scanner written in Python. It scans a specified IP range to discover devices on the local network and prints their IP and MAC addresses.

Features
Scans an IP range for active devices.
Prints the discovered IP and MAC addresses in a tabular format.
Requirements
To run this ARP scanner, you need to have Python and the scapy library installed on your system.

Python
Ensure that Python is installed on your system. You can download Python from the official Python website.

Required Libraries
The ARP scanner requires the scapy library. Install it using the following command:

bash
pip install scapy


Installation
Clone the Repository

If you haven't already, clone this repository to your local machine:

bash
git clone https://github.com/yourusername/arp-scanner.git

Navigate to the Project Directory

bash
cd arp-scanner

Install Required Libraries
Install the scapy library using pip:

bash
pip install scapy

Usage
Open the Python Script
Open the arp_scanner.py file in your favorite text editor.

Edit the IP Range

Modify the ip_range variable in the script to specify the IP range you want to scan. For example:

python
ip_range = "192.168.1.1/24"

Run the Script
Execute the script using Python:

bash
python arp_scanner.py

The script will perform an ARP scan on the specified IP range and print the results.