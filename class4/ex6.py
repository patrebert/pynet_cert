#!/bin/env python
from netmiko import ConnectHandler
"""
    Connect to three devices and display arp table using Netmiko
"""

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
}

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
    'secret': ''
}

rtr1=ConnectHandler(**pynet1)
rtr2=ConnectHandler(**pynet2)
srx=ConnectHandler(**juniper_srx)

print "\nPYNET_RTR1 ARP TABLE:\n"
print rtr1.send_command('show arp')
print "\nPYNET_RTR2 ARP TABLE:\n"
print rtr2.send_command('show arp')
print "\nPYNET-JNPR-SRX1 ARP TABLE:\n"
print srx.send_command('sho arp')



