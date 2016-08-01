#!/usr/bin/env python

import sys
import re
from ciscoconfparse import CiscoConfParse as ccp
import yaml

conf=ccp("cisco_ipsec.txt")

# create ifconfigs list (list of dictionaries)
ifconfigs=[]
for interf in conf.find_objects("interface"):
  newdict={}
  newdict[interf.text]=[]
  for child in interf.children:
    newdict[interf.text].append(child.text)
  ifconfigs.append(newdict)
print "ifconfigs=%s" %ifconfigs

# show ifconfigs
for dict in ifconfigs:
  key=dict.keys()[0]
  print key
  for conf in dict[key]:
    print conf

# write to file
with open("yaml.yml","w") as f:
  f.write(yaml.dump(ifconfigs))

# read from file
with open("yaml.yml") as f:
  newlist=yaml.load(f)

# compare to original
if newlist==ifconfigs:
  print "MATCH"
else:
  print "NO MATCH"

sys.exit()
