#!/usr/bin/env python

#pynet-sw4 eapi_username=eapi eapi_password=17mendel eapi_hostname=184.105.247.75 eapi_port=443

import sys
import jsonrpclib
import ssl
import re

def re_in_list(regex,list):
    for l in list:
        m = re.match('(%s*)' %regex, l)
        if m:
            return l
    return None


opcodes = [
    '--name',
    '--remove'
]

opcode=sys.argv.pop(1)
if not opcode in opcodes:
    print "INVALID OPERATION: USE --name or --remove"

if opcode == '--name':
    vlan_name=sys.argv.pop(1)
    vlan_num=sys.argv.pop(1)
elif opcode == '--remove':
    vlan_num = sys.argv.pop(1)
vlan_string = "vlan %s" %vlan_num


ssl._create_default_https_context = ssl._create_unverified_context

ip = '184.105.247.75'
port = '443'
username = 'eapi'
password = '17mendel'
switch_url = 'https://{}:{}@{}:{}/command-api'.format(username,password,ip,port)

remote_connect = jsonrpclib.Server(switch_url)
response = remote_connect.runCmds(1,[{'cmd': 'enable', 'input': ''}, 'show running-config'])
config = response[1]['cmds']
is_configured = re_in_list(vlan_string, config)

if opcode == '--name':
    if is_configured:
        vlan_config = config[vlan_string]['cmds']
        name = " ".join(re_in_list('name',vlan_config).split()[1:])
        print "vlan %s IS CONFIGURED" %vlan_num
        print "  NAME IS %s" %name
        if name != vlan_name:
            print "    BUT NAME IS INCORRECT"
            #Configure vlan name
            commands = []
            commands.append({'cmd': 'enable', 'input': ''})
            commands.extend(['configure terminal', 'vlan %s' %vlan_num, 'name %s' %vlan_name])
            remote_connect.runCmds(1,commands)
    else:
        print "vlan %s IS NOT CONFIGURED" %vlan_num
        commands = []
        commands.append({'cmd': 'enable', 'input': ''})
        commands.extend(['configure terminal', 'vlan %s' %vlan_num, 'name %s' %vlan_name])
        remote_connect.runCmds(1,commands)
        print "vlan %s CONFIGURED"

elif opcode=='--remove':
     if is_configured:
         commands = []
         commands.append({'cmd': 'enable', 'input': ''})
         commands.extend(['configure terminal', 'no vlan %s' %vlan_num])
         remote_connect.runCmds(1,commands)
         print "vlan %s REMOVED" %vlan_num
     else:
         print "vlan %s IS NOT CONFIGURED" %vlan_num
