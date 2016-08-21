#!/usr/bin/env python
"""
Demonstrate use of paramiko to connect to
managed device, send commands, get output
"""
import sys
import paramiko
from getpass import getpass
from time import sleep

ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'
password=getpass()
sess=paramiko.SSHClient()
sess.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sess.connect(ip_addr,username=username,password=password,
  look_for_keys=False, allow_agent=False)
rc = sess.invoke_shell()
outp = rc.recv(5000)
print outp
rc.send("show ip int brief\n")
sleep(1)
outp=rc.recv(5000)
print outp
sys.exit()
