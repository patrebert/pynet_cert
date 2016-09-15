#!/bin/env python
#pynet-sf-srx ansible_ssh_host=184.105.247.76 juniper_user=pyclass juniper_passwd=88newclass
import sys
from jnpr.junos import Device
from pprint import pprint

a_device = Device(host='184.105.247.76', user='pyclass', password='88newclass')
a_device.open()
pprint(a_device.facts)
