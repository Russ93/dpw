import urllib2
import json

#-------------------------------------------------- Views --------------------------------------------------#
class Page():
#-------------------- initializer --------------------#
	def __init__(self):
		#-------------------- Head --------------------#		
		self.__header='''
<!DOCTYPE>
<html>
	<head>
		<title></title>
		<link href='http://fonts.googleapis.com/css?family=Lato:300|Raleway' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" href="c/n.css">
		<link rel="stylesheet" href="c/m.css">
		<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.js"></script>
		<script>$(document).ready(function(){$("#zip").keydown(function(e){-1!==$.inArray(e.keyCode,[46,8,9,27,13,190])||65==e.keyCode&&e.ctrlKey===!0||e.keyCode>=35&&e.keyCode<=39||(e.shiftKey||(e.keyCode<48||e.keyCode>57)&&(e.keyCode<96||e.keyCode>105))&&e.preventDefault()})});</script>
	</head>
	<body>'''
		#-------------------- Buttons --------------------#
		self.__nav='''
			<nav>
				<img src='i/logo.png' />
				<form>
					<input type='text' name='zip' placeholder='Enter the zip code for local deals' id='zip' maxlength="5" required='required' />
					<button>Submit</button>
				</form>
			</nav>'''
		self.__cta='''
	<div id='cta'>
		<h1>Welcome to</h1>
		<img src='i/logo.png' />
		<p>You're one stop for a great combination of Living Social, Groupon, and all Local Stores. Just enter you're zip code below and get all of the great deals with a 20 miles radius of where you live.</p>
		<form>
			<input type="text" name="zip" placeholder="Enter the zip code for local deals" id='zip' maxlength="5" required='required' />
			<button>Submit</button>
		</form>
	</div>
		'''
		#-------------------- Closers --------------------#
		self.__foot='''
	</body>
</html>'''
#-------------------- Returners --------------------#
	@property
	def head(self):
		return self.__header
	@property
	def nav(self):
		return self.__nav
	@property
	def cta(self):
		return self.__cta
	@property
	def template(self):
		return self.__tmp
	@property
	def foot(self):
		return self.__foot
	@property
	def ul(self):
		return self.__ul
	@ul.setter
	def ul(self, val):
		self.__ul = val
#-------------------- Templater --------------------#
	def tmp(self,arr):
		tmp = u''
		for uil in arr:
			# Creates the list item
			currentObject = u'''
			<li>
				<a href='{uil[homepage]}' target="_blank" class='nomarg'><img class="logo" src="{uil[showLogo]}" /></a>
				<a href='{uil[URL]}' target='_blank' class='nomarg'><img class='big' src='{uil[showImageStandardBig]}' /></a>
				<h3>{uil[name]}</h3>
				<h4>{uil[dealTitle]}</h4>
				<p>{uil[dealinfo]}</p>
				<address>{uil[address]}.<br/>{uil[city]}, {uil[state]}</address>
			</li>'''
			tmp = tmp + currentObject.format(**locals())
		# Wraps it in the Unordered List
		ul = '''
			<ul>'''+tmp+'''
			</ul>
		'''
		# sets the .__ul 
		self.ul = ul