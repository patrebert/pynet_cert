#!/bin/env python
from net_system.models import NetworkDevice
import django
from netmiko import ConnectHandler
from datetime import datetime

import threading
import time

def show_ver(device):
    creds = device.credentials
    remote_conn = ConnectHandler(
        device_type=device.device_type, 
        ip=device.ip_address,
        username=creds.username,
        password=creds.password,
        port=device.port,
        secret=''
    )
    print
    print '#' * 80
    print remote_conn.send_command("show version")
    print '#' * 80
    print

def main():
    django.setup()

    devices=NetworkDevice.objects.all()
    start_time=datetime.now()
    for device in devices:
        my_thread = threading.Thread(target=show_ver, args=(device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()
    elapsed_time=datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)
if __name__ == "__main__":
    main()
