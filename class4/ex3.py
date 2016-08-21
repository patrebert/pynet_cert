#!/bin/env python
from session import session

sess1 = session('184.105.247.71')
sess1.connect('pyclass','88newclass')
for line in sess1.sendCmd('show ip int brief'):
    print line.rstrip()
sess1.disco()
