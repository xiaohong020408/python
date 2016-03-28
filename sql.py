#for mysql5.5 binlog
import os,sys
#python binlog.py binglog-0001 '2013-07-01 00:00:00' '2013-07-02 00:00:00'
def log_w(type,text):
    logfile = "%s.txt" % (type,text)
    #now = time.strftime("%Y-%m-%d %H:%M:%S")
    tt = str(text) + "\n"
    f = open(logfile,'a+')
    f.write(tt)
    f.close()
logname = sys.argv[1]
#start_time = sys.argv[2]
#end_time = sys.argv[3]
#comn = "mysqlbinlog --start-datetime='%s' --stop-datetime='%s' %s" % (start_time,end_time,logname)
#aa=os.popen(comn).readlines()

mylist=[]
i=0

f=open(logname)
while True:
    a=f.readline()
    if a:
        i=i+1
        if i % 10000 == 0:
            print i,"\n"
    else:
        break

    if ('UPDATE' in a):
            update = ' '.join(a.split()[:2])
            mylist.append(update)
    if ('INSERT INTO' in a):
            update = ' '.join(a.split()[:3]).replace("INTO ","")
            mylist.append(update)
    if ('DELETE from' in a):
            update = ' '.join(a.split()[:3]).replace("from ","")
            mylist.append(update)
mylist.sort()
bb = list(set(mylist))
bb.sort()
cc = []
for item in bb:
        cc.append([mylist.count(item),(item)])
cc.sort()
cc.reverse()
for i in cc:
        print str(i[0])+'\t'+i[1]


