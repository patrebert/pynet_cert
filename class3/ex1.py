#!/bin/env python
import sys
import snmp_helper
import time
import email_helper
import pickle

def delta(intList):
    print "DELTA: intList=%s" %intList
    retList=[]
    for i in range(len(intList)-1):
        retList.append(intList[i+1]-intList[i])
    return retList

def addNone(alist,nmod):
    rlist=[]
    for n in range(len(alist)):
        if n%nmod:
            rlist.append(None)
        else:
            rlist.append(alist[n])
    return rlist

oids = [
    ('ccmHistoryRunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0'),
    ('ccmHistoryRunningLastSaved', '1.3.6.1.4.1.9.9.43.1.1.2.0'),
    ('ccmHisoryStartupLastChanged', '1.3.6.1.4.1.9.9.43.1.1.3.0')
]

#sleep_time=int(sys.argv.pop())
#niter=int(sys.argv.pop())
sleep_time=60
niter=17

ip = "184.105.247.71"
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user=(a_user, auth_key, encrypt_key)
pynet_rtr1 = (ip,161)

count = 0
plot_lists = {}

# Create results dictionary
for oid in oids:
    plot_lists[oid[0]]=[]

timestamps = []
results = {}
lastres=None
recipient='patrebert@yahoo.com'
subject='Router Configuration Change (%s)' %ip
sender='prebert@pylab8b.twb-tech.com'
while count<niter:
    timestamps.append(time.ctime().split()[3])
    print "\nCount %d" %count
    for oid in oids:
        pname=oid[0]
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1,snmp_user,oid = oid[1])
        output=snmp_helper.snmp_extract(snmp_data)
        results[oid[0]]=int(output)
        if not lastres:
            lastres=results['ccmHistoryRunningLastChanged']
        if results['ccmHistoryRunningLastChanged'] != lastres:
            lastres=results['ccmHistoryRunningLastChanged']
            print "CONFIG CHANGED. SEND EMAIL"
            message="Configuration changed at uptime %d" %lastres
            email_helper.send_mail(recipient, subject, message, sender)
    count+=1
    print "results=%s" %results
    time.sleep(sleep_time)

pickle.dump(results,open("save_results.p","wb"))
saved_results = pickle.load(open("save_results.p","rb"))
print "\nsaved_results=%s" %saved_results
if results == saved_results:
    print "\nPICKLE WORKS; results match saved results"
else:
    print "\nSAVED RESULTS DO NOT MATCH RESULTS"
sys.exit()
