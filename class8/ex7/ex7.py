#!/bin/env python
from net_system.models import NetworkDevice
import django
from netmiko import ConnectHandler
from datetime import datetime

from multiprocessing import Process, current_process
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
    procs=[]
    start_time=datetime.now()
    for device in devices:
        my_proc = Process(target=show_ver, args=(device,))
        my_proc.start()
        procs.append(my_proc)

    for proc in procs:
        print proc
        proc.join()

    elapsed_time=datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)
if __name__ == "__main__":
    main()
