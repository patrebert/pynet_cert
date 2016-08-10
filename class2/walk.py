#!/usr/bin/env python
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
    cmdgen.CommunityData('server', 'galileo', 1),
    cmdgen.UdpTransportTarget(('184.105.247.70', 161)),
    cmdgen.MibVariable('IF-MIB', '').loadMibs(),
#   cmdgen.MibVariable('1.3.6.1.2.1.2'),
    lexicographicMode=True, maxRows=100,
    ignoreNonIncreasingOid=True
)

if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
            )
        )
    else:
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

