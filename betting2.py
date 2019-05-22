#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()

fs = cgi.FieldStorage()

print "Content-type: text/plain\n"
for key in fs.keys():
    print "%s = %s" % (key, fs[key].value)


print 'Content-type: text/html\r\n\r'
print '<html>'
print 
print '</html>'