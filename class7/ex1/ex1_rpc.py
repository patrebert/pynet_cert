#!/usr/bin/env python

#pynet-sw4 eapi_username=eapi eapi_password=17mendel eapi_hostname=184.105.247.75 eapi_port=443

import jsonrpclib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ip = '184.105.247.75'
port = '443'
username = 'eapi'
password = '17mendel'
switch_url = 'https://{}:{}@{}:{}/command-api'.format(username,password,ip,port)

remote_connect = jsonrpclib.Server(switch_url)
response = remote_connect.runCmds(1,['show interfaces'])

for item in response:
    print "\n"
    for ifname in sorted(item['interfaces']):
        ifDict = item['interfaces'][ifname]
        if 'interfaceCounters' in ifDict:
            counterDict=ifDict['interfaceCounters']
            print "%s %s %s" %(ifname,counterDict['inOctets'],counterDict['outOctets'])
