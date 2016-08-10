#!/usr/bin/env python
"""

2. Telnetlib
 a. Write a script that connects using telnet to the pynet-rtr1 router.
Execute the 'show ip int brief' command on the router and return the output.

184.105.247.70  pynet-rtr1  cisco (pyclass/88newclass)

Try to do this on your own (i.e. do not copy what I did previously).
You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()

"""

import telnetlib as tnl
import sys
import socket
import time
import re


class Session:
    """
    Connect to and operate on device
    """

    def __init__(self, ipaddr, port, timeout, username, password):
        self.sess = None
        self.ipaddr = ipaddr
        self.port = port
        self.timeout = timeout
        self.open_status = None
        try:
            self.sess = tnl.Telnet(ipaddr, port, timeout)
        except socket.timeout:
            self.open_status = 'socket.timeout'
            return None
        output = self.sess.read_until('sername:', timeout)
        print output
        self.sess.write("%s\n" %username)
        output = self.sess.read_until('assword:', timeout)
        print output
        self.sess.write("%s\n" %password)
#       time.sleep(9)
        output = self.sess.read_some()
        for line in output.split('\n'):
            print line.rstrip()
        if re.search("Authentication failed", output):
            self.open_status = "Authentication failed"
        print output
        return None

    def send_command(self, command):
        """
        Send command to open session
        """
        self.sess.write("%s\n" %command.rstrip())
        time.sleep(1)
        return self.sess.read_very_eager()


TELNET_PORT = 23
TELNET_TIMEOUT = 6
def main():
    """
    Connect to hard coded device with telnetlib
    Get "show ip int brief" output
    """
    ipaddr = "184.105.247.70"
    username = "pyclass"
    password = "88newclass"

    sess = Session(ipaddr, TELNET_PORT, TELNET_TIMEOUT, username, password)
    if sess.open_status:
        print "SESSION OPEN FAILURE: %s" %sess.open_status
        sys.exit()
    output = sess.send_command("sho ip int br")
    print output
    sys.exit()

if __name__ == "__main__":
    main()
