#!/bin/env python
from net_system.models import NetworkDevice, Credentials
devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

for device in devices:
    print device.device_name
    if 'rtr' in device.device_name:
        print "  Vendor Cisco"
        device.vendor = "Cisco"
    elif 'pynet-sw' in device.device_name:
        print "  Vendor Arista"
        device.vendor = "Arista"
    elif 'juniper' in device.device_name:
        print "  Vendor Juniper"
        device.vendor = "Juniper"
    else:
        print "  UNKNOWN VENDOR"
    device.save()

for device in devices:
    print "%s %s" %(device.device_name, device.vendor)
