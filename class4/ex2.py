#!/usr/bin/env python
"""
Demonstrate use of paramiko to connect to
managed device, send commands, get output
"""
import sys
import paramiko
from getpass import getpass
from time import sleep

ip_addr = '184.105.247.71'
username = 'pyclass'
password = '88newclass'
#password=getpass()
sess=paramiko.SSHClient()
#sess.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sess.load_system_host_keys() # use known_hosts entries

sess.connect(ip_addr,username=username,password=password,
  look_for_keys=False, allow_agent=False)
rc = sess.invoke_shell()
rc.settimeout(5.0)
outp = rc.recv(5000)
print outp
rc.send("term len 0\n")
sleep(1)
outp=rc.recv(5000)
print outp

rc.send("config t\n")
sleep(1)
outp=rc.recv(5000)
print outp
rc.send("logging buffered 10000\n")
sleep(1)
rc.send("end\n")
sleep(1)
outp=rc.recv(5000)
print outp
rc.send("sho run | i logging\n")
sleep(1)
outp=rc.recv(5000)
print outp
sys.exit()
