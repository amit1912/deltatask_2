import os

import sys

from crontab import CronTab

total = len(sys.argv)


cmdargs = str(sys.argv)
arg1 = sys.argv[1]
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)

file_name = 'delta1.py'
path = os.path.join(arg1, file_name)


with open(path, 'wb') as f:

     f.write('import MySQLdb\n')
     f.write('db = MySQLdb.connect("localhost","root","abc123")\n')
     f.write('cursor = db.cursor()\n')
     f.write("sql1 = ' CREATE DATABASE NEW_DB '\n")
     f.write('cursor.execute(sql1)\n')
     f.write("cursor.execute('USE NEW_DB')\n")
     f.write('sql = """CREATE TABLE TASK(DATE_COl  VARCHAR(100) )"""\n')
     f.write('cursor.execute(sql)\n')
     f.write('db.commit()\n')
     f.write('db.close()\n')
f.close()



file2_name = 'delta2.py'
path = os.path.join(arg1, file2_name)
with open(path, 'wb') as g:
     g.write('import MySQLdb\n')
     g.write('from time import gmtime, strftime\n')
     g.write('db = MySQLdb.connect("localhost","root","abc123","NEW_DB")\n')
     g.write('cursor = db.cursor()\n')
     g.write('CURTIME =  strftime("%H:%M:%S", gmtime())\n')
     g.write('sql = """INSERT INTO TASK(DATE_COl)VALUES (CURTIME())"""\n')
     g.write("cursor.execute(sql)\n")
     g.write('db.commit()\n')
     g.write('db.rollback()\n')
     g.write('db.close()\n')
g.close()

tab = CronTab(user='root',fake_tab='True')
cmd = '/var/www/pjr-env/bin/python  path'
cron_job = tab.new(cmd)
cron_job.minute().every(10)
tab.write()
print tab.render()
