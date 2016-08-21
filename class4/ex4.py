#!/bin/env python
from session import session

sess1 = session('184.105.247.71')
sess1.connect('pyclass','88newclass')

for line in sess1.sendCmd('config t'):
    print line.rstrip()
for line in sess1.sendCmd('logging buffer 10000'):
    print line
for line in sess1.sendCmd('end'):
    print line
for line in sess1.sendCmd('sho run | i logging'):
    print line
sess1.disco()
