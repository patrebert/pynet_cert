from net_system.models import NetworkDevice
import django
from netmiko import ConnectHandler
from datetime import datetime

def main():
    django.setup()

    devices=NetworkDevice.objects.all()
    start_time=datetime.now()
    for device in devices:
        creds=device.credentials
        print "\n########## %s ###########" %device.device_name
        sess1=ConnectHandler(
            ip=device.ip_address,
            username = creds.username,
            password = creds.password,
            device_type = device.device_type
        )
        for line in sess1.send_command_expect("show version").split("\n"):
            print line.rstrip()
    elapsed_time=datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)
if __name__ == "__main__":
    main()
