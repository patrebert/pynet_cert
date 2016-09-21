
from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    devices=NetworkDevice.objects.all()
    for device in devices:
        print device.device_name
if __name__ == "__main__":
    main()
