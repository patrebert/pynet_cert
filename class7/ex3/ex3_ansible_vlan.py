#!/usr/bin/env python

#pynet-sw4 eapi_username=eapi eapi_password=17mendel eapi_hostname=184.105.247.75 eapi_port=443

import sys
import pyeapi
import ssl
import re

def re_in_list(regex,list):
    for l in list:
        m = re.match('(%s*)' %regex, l)
        if m:
            return l
    return None

def main():

   '''
    Simple Ansible module to create an Arista VLAN
    '''

    module = AnsibleModule(
        argument_spec=dict(
            arista_sw=dict(required=True),
            vlan_id=dict(required=True),
            vlan_name=dict(required=False),
        )
    )

    vlan_string = "vlan %s" %vlan_id
    name_string = "name %s" %vlan_name


    ssl._create_default_https_context = ssl._create_unverified_context

    remote_connect=pyeapi.connect_to("pynet-sw4")
    response=remote_connect.enable("show running-config")
    config=response[0]['result']['cmds']
    if vlan_string in config.keys():
        is_configured = True
        vlan_config = config[vlan_string]
    else:
        is_configured = False

    if opcode == '--name':
        if is_configured:
            print "vlan %s IS CONFIGURED" %vlan_num
            print "  NAME IS %s" %name_string
            if not name_string in vlan_config.keys():
                print "    BUT NAME IS INCORRECT"
                print "RECONFIGURE VLAN NAME"
                commands = [vlan_string,name_string]
                print "COMMANDS=%s" %commands
                remote_connect.config(commands)
        else:
            print "vlan %s IS NOT CONFIGURED" %vlan_num
            commands = [vlan_string,name_string]
            print "COMMANDS=%s" %commands
            remote_connect.config(commands)
            print "vlan %s CONFIGURED" %vlan_num

    elif opcode=='--remove':
        if is_configured:
             commands = ['no %s' %vlan_string]
             remote_connect.config(commands)
             print "vlan %s REMOVED" %vlan_num
        else:
            print "vlan %s IS NOT CONFIGURED" %vlan_num

if __name__ == "__main__":
    main()
