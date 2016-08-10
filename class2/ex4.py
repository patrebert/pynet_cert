#!/usr/bin/env python

"""
read hosts format device names from stdin (ip,name)
get sysName, sysDescr
"""

import fileinput
from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = '184.105.247.70'
OID = '.1.3.6.1.2.1.1.1.0'

for line in fileinput.input():
    print "\n%s" %line
    devip = line.split()[0]
    a_device = (devip, COMMUNITY_STRING, SNMP_PORT)
    snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.1.0')
    output = snmp_extract(snmp_data)
    print output
    output = snmp_extract(snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.5.0'))
    print ""
    print output
