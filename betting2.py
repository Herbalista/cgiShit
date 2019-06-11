#!/usr/bin/python

import cgi
import cgitb
import math

cgitb.enable()

"""fs = cgi.FieldStorage()
a = []
print "Content-type: text/plain\n"
for key in fs.keys():
    print "%s = %s" % (key, fs[key].value)

a = cgi.FieldStorage("b1o1")"""
form = cgi.FieldStorage()
b1o1 = float(form.getvalue("b1o1"))
b1o2 = float(form.getvalue("b1o2"))
b2o1 = float(form.getvalue("b2o1"))
b2o2 = float(form.getvalue("b2o2"))
stake = float(form.getvalue("stake"))
outcome = float
outcome = math.pow(b1o1,-1)

checkOne = float
checkTwo = float
betOne = float
betTwo = float
betThree = float
betFour = float

checkOne = math.pow(b1o1,-1) + math.pow(b2o2, -1)
checkTwo = math.pow(b1o2,-1) + math.pow(b2o1, -1)

if checkOne < 1 and checkTwo > 1:
	betOne = stake/b1o1
	betTwo = stake/b2o2
	winning = float
	winning = stake-(betOne+betTwo)
	print "Content-type: text/html"
	print """
	<html>
	<title>Calculator</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="mystylesheet.css" type="text/css">
	<style>
	body{
		background-color: #05ffb0;
	}
	</style>
	<body>

	<div class="container">
	  <h1>Arbitage betting calculator</h1>
	</div>
	<p>If you set  </p>
	"""
	print betOne 
	print '<p>on Bookmaker 1 Outcome 1 and  </p>'
	print betTwo
	print '<p>on Bookmaker 2 Outcome 2 you win </p>'
	print winning
	print '<p>wich brings you to your initial  </p>'
	print stake

	print"""

	</body>
	<footer>
	  <p>
	    <a href="http://jigsaw.w3.org/css-validator/check/referer">
	        <img style="border:0;width:88px;height:31px"
	            src="http://jigsaw.w3.org/css-validator/images/vcss"
	            alt="CSS ist valide!" />
	    </a>
	</p>
	            
	CSS ist valide!
	<p>
	<a href="http://jigsaw.w3.org/css-validator/check/referer">
	    <img style="border:0;width:88px;height:31px"
	        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
	        alt="CSS ist valide!" />
	    </a>
	</p>
	</footer>
	</html> 
	"""
if checkTwo < 1 and checkOne >1:
	betThree = stake/b1o2
	betFour = stake/b2o1
	winning = float
	winning = stake-(betThree+betFour)
	print "Content-type: text/html"
	print """
	<html>
	<title>Calculator</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="mystylesheet.css" type="text/css">
	<style>
	body{
		background-color: #05ffb0;
	}
	</style>
	<body>

	<div class="container">
	  <h1>Arbitage betting calculator</h1>
	</div>
	<p>If you set  </p>
	"""
	print betThree 
	print '<p>on Bookmaker 1 Outcome 2 and  </p>'
	print betFour
	print '<p>on Bookmaker 2 Outcome 1 you win </p>'
	print winning
	print '<p>wich brings you to your initial  </p>'
	print stake

	print"""

	</body>
	<footer>
	  <p>
	    <a href="http://jigsaw.w3.org/css-validator/check/referer">
	        <img style="border:0;width:88px;height:31px"
	            src="http://jigsaw.w3.org/css-validator/images/vcss"
	            alt="CSS ist valide!" />
	    </a>
	</p>
	            
	CSS ist valide!
	<p>
	<a href="http://jigsaw.w3.org/css-validator/check/referer">
	    <img style="border:0;width:88px;height:31px"
	        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
	        alt="CSS ist valide!" />
	    </a>
	</p>
	</footer>
	</html> 
	"""
if checkTwo and checkOne <1:
	betOne = stake/b1o1
	betTwo = stake/b2o2
	betThree = stake/b1o2
	betFour = stake/b2o1
	winning = float
	winning = stake-(betOne+betTwo)
	winningTwo = float
	winningTwo = stake -(betThree+betFour)
	print "Content-type: text/html"
	print """
	<html>
	<title>Calculator</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="mystylesheet.css" type="text/css">
	<style>
	body{
		background-color: #05ffb0;
	}
	</style>
	<body>

	<div class="container">
	  <h1>Arbitage betting calculator</h1>
	</div>
	<p>If you set  </p>
	"""
	print betOne 
	print '<p>on Bookmaker 1 Outcome 1 and  </p>'
	print betTwo
	print '<p>on Bookmaker 2 Outcome 2 you win </p>'
	print winning
	print '<p>wich brings you to your initial  </p>'
	print stake
	print '<p>Or you bet the other way around  </p>'
	print '<p>If you set  </p>'
	print betThree 
	print '<p>on Bookmaker 1 Outcome 2 and  </p>'
	print betFour
	print '<p>on Bookmaker 2 Outcome 1 you win </p>'
	print winning
	print '<p>wich brings you to your initial  </p>'
	print stake

	print"""

	</body>
	<footer>
	  <p>
	    <a href="http://jigsaw.w3.org/css-validator/check/referer">
	        <img style="border:0;width:88px;height:31px"
	            src="http://jigsaw.w3.org/css-validator/images/vcss"
	            alt="CSS ist valide!" />
	    </a>
	</p>
	            
	CSS ist valide!
	<p>
	<a href="http://jigsaw.w3.org/css-validator/check/referer">
	    <img style="border:0;width:88px;height:31px"
	        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
	        alt="CSS ist valide!" />
	    </a>
	</p>
	</footer>
	</html> 
	"""