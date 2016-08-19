#!/bin/env python
"""
  Demonstrate gathering of interface stats and generation of plot
"""
import sys
import time
import snmp_helper
import pygal

def delta(intList):
    retList = []
    for i in range(len(intList)-1):
        retList.append(intList[i+1]-intList[i])
    return retList

def addNone(alist, nmod):
    rlist = []
    n = 0
    for a in alist:
        if n%nmod:
            rlist.append(None)
        else:
            rlist.append(a)
        n += 1
    return rlist

def plot_data(oids,plot_lists,chart):
    print "PLOT_DATA:OIDS=%s" %oids
    for oid in oids:
        print "OID[0]=%s" %oid[0]
        results = [int(res) for res in plot_lists[oid[0]]]
        print "%s: %s" %(oid[0], delta(results))
        chart.add(oid[0], delta(results))
    return chart

oids = [
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5'),
]

def main():
#   sleep_time = int(sys.argv.pop())
#   niter = int(sys.argv.pop())
    sleep_time=300
    niter=14
    ip = "184.105.247.70"
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (ip, 161)

    count = 0
    plot_lists = {}
    line_chart_1 = pygal.Line()
    line_chart_2 = pygal.Line()

# Create results dictionary
    for oid in oids:
        plot_lists[oid[0]] = []

    timestamps = []
    while count < niter:
#       timestamps.append(time.ctime().split()[3])
        print "\nCount %d" %count
        for oid in oids:
            pname = oid[0]
            snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=oid[1])
            output = snmp_helper.snmp_extract(snmp_data)
#           print "OUTPUT=%s" %output
            print "%s  %s %s" %(time.ctime().split()[3], oid[0], output)
            sys.stdout.flush()
            plot_lists[pname].append((output))
        count += 1
        time.sleep(sleep_time)

    timestamps=[0,5,10,15,20,25,30,35,40,45,50,55,60]
# Generate plot
    line_chart_1.title = 'Input/Output Bytes for %s' %plot_lists[oids[0][0]][0]
    line_chart_2.title = 'Input/Output Packets for %s' %plot_lists[oids[0][0]][0]
#   timestamps=addNone(timestamps,10)
#   for oid in oids[1:]:
#       results = [int(res) for res in plot_lists[oid[0]]]
#       print "%s: %s" %(oid[0], delta(results))
#       line_chart.add(oid[0], delta(results))
    print "OIDS=%s" %oids[1:3]
    line_chart_1.x_labels = timestamps
    line_chart_1 = plot_data(oids[1:3],plot_lists,line_chart_1)
    line_chart_1.render_to_file('test1.svg')

    line_chart_2.x_labels = timestamps
    line_chart_2 = plot_data(oids[3:],plot_lists,line_chart_2)
    line_chart_2.render_to_file('test2.svg')

if __name__ == '__main__':
    main()
