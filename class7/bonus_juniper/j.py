#!/bin/env python
#pynet-sf-srx ansible_ssh_host=184.105.247.76 juniper_user=pyclass juniper_passwd=88newclass
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.phyport import PhyPortTable
from jnpr.junos.op.phyport import PhyPortStatsTable
from getpass import getpass
from pprint import pprint

a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()
ports = EthPortTable(a_device)
jports=ports.get()
pprint(jports)
#pprint(jports['fe-0/0/1'].items())
phy_ports = PhyPortTable(a_device)
pp = phy_ports.get() 
print "PP type %s" %type(pp)
p = pp.items()
for key,values in p:
    print key 
    for k,v in values:
        print "  %s %s" %(k,v)

port_stats = PhyPortStatsTable(a_device)
ps = port_stats.get()
p = ps.items()
for key,values in p:
    print key
    for k,v in values:
        print "  %s %s" %(k,v)

