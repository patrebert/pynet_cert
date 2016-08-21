#!/bin/env python
"""
  Demonstrate use of netmiko to change configuration of device
  using configuration file
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

for device in [pynet1,pynet2]:
    print "\nDEVICE %s" %device['ip']
    sess=ConnectHandler(**device)
    print sess.config_mode()
    print sess.send_config_from_file('config.txt')
    print "%s" %sess.send_command('sho run | i logging')
    sess.disconnect()
