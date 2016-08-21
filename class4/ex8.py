#!/bin/env python
"""
  Demonstrate use of netmiko to change configuration of device
"""

from netmiko import ConnectHandler

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

sess1=ConnectHandler(**pynet2)
sess1.config_mode()
print "CONFIG MODE %s" %sess1.check_config_mode()

for device in [pynet1,pynet2]:
    print "\nDEVICE %s" %device['ip']
    sess=ConnectHandler(**device)
    sess.config_mode()
    sess.send_config_from_file('config.txt')
    print "%s" %sess.send_command('sho run | i logging')
    sess.disconnect()
    
