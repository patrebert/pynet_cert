#!/usr/bin/env python
"""
Demonstrate use of pysnmp walks
"""

import sys
import re
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

devip = sys.argv.pop(1)

errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
    cmdgen.CommunityData('server', 'galileo', 1),
    cmdgen.UdpTransportTarget((devip, 161)),
    cmdgen.MibVariable('IF-MIB', '').loadMibs(),
    lexicographicMode=True, maxRows=150
)

if errorIndication:
    print errorIndication
else:
    if errorStatus:
        print '%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
            )

    else:
        ifdescr = []
        inoctets = []
        outoctets = []
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                np = name.prettyPrint()
                vp = val.prettyPrint()
                if re.search(r"ifDescr\.\d+", np):
                    ifdescr.append(vp)
                    continue
                if re.search(r"ifInOctets\.\d+", np):
                    inoctets.append(vp)
                    continue
                if re.search(r"ifOutOctets\.\d+", np):
                    outoctets.append(vp)
        for l in zip(ifdescr, inoctets, outoctets):
            print "%s\t%s\t%s" %(l[0], l[1], l[2])
