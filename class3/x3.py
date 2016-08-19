#!/bin/env python
import sys
import pygal

def addNone(alist,nmod):
    rlist=[]
    for n in range(len(alist)):
        if n%nmod:
            rlist.append(None)
        else:
            rlist.append(alist[n])
    return rlist

niter=int(sys.argv.pop())
line_chart = pygal.Line()
line_chart.title = 'Input/Output Packets and Bytes'

n=0
timestamps=[]
data=[]
while n<niter:
    timestamps.append("00:%02d:00" %n)
    data.append(n)
    n+=1
# Generate plot
#timestamps=addNone(timestamps,2)
print "TIMESTAMPS=%s" %timestamps
line_chart.x_labels=timestamps
line_chart.add('data',data)
line_chart.render_to_file('t.svg')
