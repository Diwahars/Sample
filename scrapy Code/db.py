#!/usr/bin/env python
import ConfigParser
import os
import time
import getpass

def get_dump():
    print "Enter user:"
    user = 'root'

    print "Password will not be visible:"
    password = 'root'

    print "Enter host:"
    host = 'localhost'

    print "Enter database name:"
    database = 'csl_assignment'


    filestamp = time.strftime('%Y-%m-%d-%I:%M')
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (user,password,host,database,database+"_"+filestamp))
    
    print "\n-- please have a the dump file in "+database+"_"+filestamp+".gz --"

if __name__=="__main__":
    get_dump()
