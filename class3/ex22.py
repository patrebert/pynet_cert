#!/bin/env python
import sys
import snmp_helper
import time
import pygal

def delta(intList):
    print "DELTA: intList=%s" %intList
    retList=[]
    for i in range(len(intList)-1):
        retList.append(intList[i+1]-intList[i])
    return retList

def x_labels(alist,nmod):
    rlist=[]
    for n in range(len(alist)):
        if not n%nmod:
            rlist.append(alist[n])
    return rlist

oids = [
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5'),
]

sleep_time=int(sys.argv.pop())
niter=int(sys.argv.pop())
ip = "184.105.247.70"
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user=(a_user, auth_key, encrypt_key)
pynet_rtr1 = (ip,161)

count = 0
plot_lists = {}
line_chart = pygal.Line(include_x_axis=True, show_minor_x_labels=False)
line_chart.title = 'Input/Output Packets and Bytes for %s' %oids[0][1]

# Create results dictionary
for oid in oids:
    plot_lists[oid[0]]=[]

# Get results
timestamps = []
while count<niter:
    timestamps.append(time.ctime().split()[3])
    print "\nCount %d" %count
    for oid in oids:
        pname=oid[0]
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1,snmp_user,oid = oid[1])
        output=snmp_helper.snmp_extract(snmp_data)
        print "OUTPUT=%s" %output
        print "%s  %s %s" %(time.ctime().split()[3],oid[0],output)
        plot_lists[pname].append((output))
    count+=1
    time.sleep(sleep_time)

# Generate plot
line_chart.title = 'Input/Output Packets and Bytes for %s' %plot_lists[oids[0][0]][0]
x_major_labels=x_labels(timestamps,(len(timestamps)+1)/5)
print "x_major_labels=%s" %x_major_labels
line_chart.x_labels = timestamps
line_chart.x_labels_major=x_labels(timestamps,3)

for oid in oids[1:]:
  results = [int(res) for res in plot_lists[oid[0]]]
  print "%s: %s" %(oid[0],delta(results))
  line_chart.add(oid[0],delta(results))
line_chart.render_to_file('test.svg')
