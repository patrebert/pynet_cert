
from net_system.models import NetworkDevice
import django

def main():
    django.setup()

#   pynet_rtr3 = NetworkDevice(
#       device_name='new-rtr3',
#       device_type='cisco_ios',
#       ip_address='184.105.247.80',
#       port=22,
#   )
#   pynet_rtr3.save()

    pynet_rtr4 = NetworkDevice.objects.get_or_create(
        device_name='new-rtr4',
        device_type='cisco_ios',
        ip_address='184.105.247.71',
        port=22,
    )
    print pynet_rtr4

    devices=NetworkDevice.objects.all()
    for device in devices:
        print "%s %s" %(device.device_name,device.ip_address)

if __name__ == "__main__":
    main()
