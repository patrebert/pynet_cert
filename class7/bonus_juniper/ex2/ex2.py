#!/bin/env python
#pynet-sf-srx ansible_ssh_host=184.105.247.76 juniper_user=pyclass juniper_passwd=88newclass

import sys
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable

def get_item(itemlist,key):
    for k,v in itemlist:
        if k==key:
            return v
    return None

a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()
ports = EthPortTable(a_device)
jports=ports.get()
items=jports.items()
for key,itemlist in items:
    print key
    for k in ['oper','rx_packets','tx_packets']:
        print "  %s %s" %(k,get_item(itemlist,k))
