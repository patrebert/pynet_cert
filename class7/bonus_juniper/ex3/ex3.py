#!/bin/env python
#pynet-sf-srx ansible_ssh_host=184.105.247.76 juniper_user=pyclass juniper_passwd=88newclass
import sys
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable

a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()

route_table = RouteTable(a_device)
rt = route_table.get()
routes = rt.items()

print "\n"
for key,values in routes:
    print key 
    for k,v in values:
        print "  %s %s" %(k,v)

