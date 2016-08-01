#!/usr/bin/env python

import sys
import re
from ciscoconfparse import CiscoConfParse as ccp
import json

conf=ccp("cisco_ipsec.txt")

# create ifconfigs list (list of dictionaries)
ifconfigs=[]
for interf in conf.find_objects("interface"):
  newdict={}
  newdict[interf.text]=[]
  for child in interf.children:
    newdict[interf.text].append(child.text)
  ifconfigs.append(newdict)

# show ifconfigs
for dict in ifconfigs:
  key=dict.keys()[0]
  print key
  for conf in dict[key]:print conf

# write to file
with open("json.json","w") as f:
  json.dump(ifconfigs,f)

# read from file
with open("json.json") as f:
  newlist=json.load(f)

# compare to original
if newlist==ifconfigs:
  print "\nMATCH"
else:
  print "\nNO MATCH"

sys.exit()
