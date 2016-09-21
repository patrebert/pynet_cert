#!/bin/env python
from net_system.models import NetworkDevice
import django
from netmiko import ConnectHandler
from datetime import datetime

from multiprocessing import Process, current_process, Queue
import time

def show_ver(device, q):
    output_dict = {}
    creds = device.credentials
    remote_conn = ConnectHandler(
        device_type=device.device_type, 
        ip=device.ip_address,
        username=creds.username,
        password=creds.password,
        port=device.port,
        secret=''
    )
    output = ('#' * 80) + "\n"
    output += remote_conn.send_command("show version")
    output += ('#' * 80) + "\n"
    output_dict[device.device_name] = output
    q.put(output_dict)

def main():
    django.setup()

    devices=NetworkDevice.objects.all()
    procs=[]
    start_time=datetime.now()
    q = Queue(maxsize=20)
    for device in devices:
        my_proc = Process(target=show_ver, args=(device, q))
        my_proc.start()
        procs.append(my_proc)

    for proc in procs:
        print proc
        proc.join()

    while not q.empty():
        my_dict = q.get()
        for k,v in my_dict.iteritems():
            print k
            print v
    elapsed_time=datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)

if __name__ == "__main__":
    main()
