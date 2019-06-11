#!/usr/bin/python
import cgi

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


"""
print """

<div>
    <p>Betting arbitrage ("miraclebets", "surebets", sports arbitrage) is an example of arbitrage arising on betting markets due to either bookmakers' differing opinions on event outcomes or errors. When conditions allow, by placing one bet per each outcome with different betting companies, the bettor can make a profit regardless of the outcome. Mathematically arbitrage occurs when there are a set of odds, which represent all mutually exclusive outcomes that cover all state space possibilities (i.e. all outcomes) of an event, whose implied probabilities add up to less than 1.[1] In the bettors' slang an arbitrage is often referred to as an arb; people who use arbitrage are called arbers</p>
 </div>

<div class="container">
  <h1>betting information</h1>
  <h2>Please enter the odds (Outcome of bookmaker one and bookmaker two) and the amount of money you want to bet into the inputs below
  </h2>
  <p>Please note that the odds needs to be entered in decimal with point seperation</p>
</div>

"""

#from tutorial not necessary

form = cgi.FieldStorage() 



# Using HTML input and forms method 
print("<form method='GET' action='betting2.py'>") 
print("<p>Bookmaker1 Outcome1: <input type='number' step='0.01' name='b1o1' /></p>") 
print("<p>Bookmaker1 Outcome2: <input type='number' step='0.01' name='b1o2' /></p>") 
print("<p>Bookmaker2 Outcome1: <input type='number' step='0.01' name='b2o1' /></p>") 
print("<p>Bookmaker2 Outcome2: <input type='number' step='0.01' name='b2o2' /></p>") 
print("<p>Stake: <input type='number' step='0.01' name='stake' /></p>") 
print("<input type='submit' value='Submit' />") 
print("</form") 
print("</body></html>") 



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