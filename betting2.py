#!/usr/bin/python

import cgi
import cgitb
import urllib.parse as urlparse
cgitb.enable()

fs = cgi.FieldStorage()

print "Content-type: text/plain\n"


url = cgi.FieldStorage()

parsed = urlparse.urlparse(url)
print urlparse.parse_qs(parsed.query)['def']

print 'Content-type: text/html\r\n\r'
print '<html>'
print b1o1
print '</html>'