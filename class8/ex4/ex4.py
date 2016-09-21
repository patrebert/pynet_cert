
from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    devices=NetworkDevice.objects.all()
    for device in devices:
        print "%s %s" %(device.device_name,device.ip_address)
        if 'new' in device.device_name:
            print "  DELETE THIS DEVICE"
            device.delete()
    print "\nMODIFIED DEVICE LIST:"
    for device in devices:
        print device.device_name
if __name__ == "__main__":
    main()
