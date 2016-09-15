#!/usr/bin/env python

#pynet-sw4 eapi_username=eapi eapi_password=17mendel eapi_hostname=184.105.247.75 eapi_port=443

import jsonrpclib
import pyeapi
import ssl
import sys

ssl._create_default_https_context = ssl._create_unverified_context

remote_connect = pyeapi.connect_to("pynet-sw4")
response = remote_connect.enable('show interfaces')
interfaces=response[0]['result']['interfaces']
for interface in interfaces.keys():
    print "interface %s" %interface
    ifconfig=interfaces[interface]
    if 'interfaceCounters' in ifconfig.keys():
        ifCounts=ifconfig['interfaceCounters']
        print "  inOctets %s outOctets %s" %(ifCounts['inOctets'],ifCounts['outOctets'])
