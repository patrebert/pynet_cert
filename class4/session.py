#
#
import pexpect
import os
import re
import sys
import time
#
class session:
  def __init__(self,ipaddr):
    self.ipaddr=ipaddr
    self.username=""
    self.password=""
#
# CONNECT
#
  def connect(self,username,password):
    sshcom="ssh -o ConnectTimeout=10 %s@%s" %(username,self.ipaddr)
    method='ssh'
#
# spawn ssh process
#
    self.child=pexpect.spawn(sshcom)
    self.child.maxread=1024
    self.child.timeout=600
#   self.child.searchwindowsize=100
#   self.child.logfile_read=sys.stdout


# look for password prompt

    while True:
      index1=self.child.expect(['assword:','(yes/no)',pexpect.TIMEOUT,pexpect.EOF])
#     print "index1=%d" %index1
      if index1==0:
        break
#     print index1

# First time ssh connect, say 'yes'

      elif index1==1:
#       print "YES"
        self.child.sendline('yes') 
      elif index1 == 2:
#       print "SESSION.CONNECT:SSH TIMEOUT"
        raise SSH_TIMEOUT

# SSH connection rejected, try telnet

      elif index1 == 3:
        self.child=pexpect.spawn('telnet %s' %self.ipaddr)
        index1=self.child.expect(['sername:',pexpect.TIMEOUT])
        if index1==0:
          self.child.sendline('%s' %username)
          index1=self.child.expect(['assword:',pexpect.TIMEOUT])
          if index1==0:
            break
#     sys.exit()
#
# send password
# allow multiple password attempts on ssh connection
# (multiple password prompts)
#
#   self.child.logfile_read=sys.stdout
    ntry=1
    if index1==0:
#     print "SEND PASSWORD" 
      time.sleep(.5)
      self.child.sendline(password)
#     self.child.logfile_read=sys.stdout
      while ntry<2:
        index2=self.child.expect(['[A-Za-z0-9\-]+\#','assword:','Connection refused'])
#       print "index2 %d" %index2
        if index2 == 0:
          break
        elif index2 == 1:
          ntry+=1
          print 'TACACS FAILURE TRY %d' %ntry
#         self.child.sendline(password)
        elif index2==2:
          print 'SSH CONNECTION REFUSED'
          return
#         sys.exit()
        if ntry==2:
          print "TACACS AUTHENTICATION FAILURE"
          return
#         sys.exit()
#
#
#   print "TERM LEN 0"
#   self.child.logfile_write=sys.stdout
    self.child.sendline('term len 0')
    ind=self.child.expect(['Unknown command','(enable)','[A-Za-z0-9\-]+\#'])
#   print "IND=%d" %ind
    if ind==0:
      self.child.sendline('set len 0')
#     print "SET LEN 0"
      self.child.expect('enable')
#   elif ind==2:
#     self.child.sendline('')
    else:
      self.child.sendline('') 
    return
  pass #CONNECT
#
# sendCmd
#
  def sendCmd(self,com):
    self.child.logfile_read=sys.stdout
#   print "COMMAND=%s" %com
#
# execute command
#
    rex1=re.compile('[A-Za-z0-9_\-\(\)]+[#]')
    rex2=re.compile('\(enable\)')
    rex3=re.compile('([!-~ ]*)\r')
#   self.child.sendline('')
#   self.child.expect(['[A-Za-z0-9]+[#]','(enable)'])
    self.child.expect([rex1,rex2])
#   print com
#   print "SEND COMMAND %s" %com
    self.child.sendline(com)
    self.child.logfile_read=None
#   sys.logfile=sys.stdout 
    while True:
      index=self.child.expect([rex1,rex2,rex3])
#     print "index=%d" %index
      if index==0:
#       print "REX1"
        self.child.sendline('') # generate another prompt
        break
      elif index==1:
#       print "REX2"
        self.child.sendline('') # generate another prompt
        break
      elif index==2:
#       print "REX3"
#       pass
#       print "line1=%s" %self.child.match.group(1).rstrip()
        yield self.child.match.group(1).rstrip()
      else:
        print "LINE NOT MATCHED"
    pass #while True
    return
  pass #sendCmd
#
# INTERACT
  def interact(self):
    self.child.interact()
#
# DISCONNECT
#
  def disco(self):
#
#
#   self.child.logfile_send=sys.stdout
    self.child.sendline('exit')
#   sys.exit()
    return
  pass #disco 
#
#
