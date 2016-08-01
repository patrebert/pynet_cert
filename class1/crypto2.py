#!/usr/bin/env python

import sys
import re
from ciscoconfparse import CiscoConfParse as ccp

# overkill for this assignment but expect to do a lot of this
def child_val(regex,cfgl_object):
  rval=None
  val=[val.text for val in cfgl_object if re.match(regex,val.text)] # list of matches,use first
  if not val:return None
  val=val[0]
  rx="%s\s+([!-~ ]+)" %regex
  m=re.match(rx,val)
  if m:
    rval=m.group(1)
  return rval

conf=ccp("cisco_ipsec.txt")

print "\nCrypto config:"
for map in conf.find_objects("crypto map CRYPTO"):
  print map.text
  for child in map.children:print child.text

print "\nMaps using pfs group 2:"
for map in conf.find_objects_w_child("crypto map CRYPTO","set pfs group2"):
  print map.text

print "\nMaps not using AES-SHA:"
for map in conf.find_objects_wo_child("crypto map CRYPTO","set transform-set AES-SHA"):
  print "%s (%s)" %(map.text,child_val(r"\s+set transform-set",map.children))

sys.exit()    
