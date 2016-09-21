#!/bin/env python
from net_system.models import NetworkDevice, Credentials
devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()
std_creds = creds[0]
arista_creds = creds[1]
for device in devices:
    print device.device_name
    if 'pynet-sw' in device.device_name:
        print "  Arista switch: use arista_creds"
        device.credentials = arista_creds
    else:
        print "  Not Arista: use std_creds"
        device.credentials = std_creds
    device.save()

for device in devices:
    print "%s %s" %(device.device_name, device.credentials)
