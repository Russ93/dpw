import urllib2
import json

#-------------------------------------------------- Model --------------------------------------------------#
class Model(object):
	def __init__(self,zip):
		self.__key = '82cb2645283a89fe53352968298a7fd61ad8386f5110836008c14e1435faf5b3a8f063a5ce613aa22b528c095b429ee2'
		self.__url = 'http://api.8coupons.com/v1/getdeals?key='+self.__key+'&zip='+zip+'&mileradius=20&limit=1000&orderby=radius&categoryid=2,6'
		#url we are going to load the page from
		self.__req = urllib2.Request(self.__url) # concat zip with url
		self.__opener = urllib2.build_opener() #magic to load request creates framework to get url
		self.__result = self.__opener.open(self.__req) #gets url and puts result in 'result'
		self.__obj = json.load(self.__result)


	@property
	def do(self):
		return self.__obj

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
		<link href='http://fonts.googleapis.com/css?family=Lato:300|Quicksand' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" href="c/n.css">
		<link rel="stylesheet" href="c/m.css">
	</head>
	<body>'''
		#-------------------- Buttons --------------------#
		self.__nav='''
			<nav>
				<h1> Ultra Coupon </h1>
				<form>
					<input type='text' name='zip' placeholder='Enter the zip code for local deals' />
					<button>Submit</button>
				</form>
			</nav>'''
		self.__cta='''
	<div id='cta'>
		<h1>Welcome to Ultra Coupon</h1>
		<p>You're one stop for a great combination of Living Social, Groupon, and all Local Stores. Just enter you're zip code below and get all of the great deals with a 20 miles radius of where you live.</p>
		<form>
			<input type="text" name="zip" placeholder="Enter the zip code for local deals">
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
				<a href='{uil[homepage]}'><img class="logo" src="{uil[showLogo]}" /></a>
				<a href='{uil[URL]}'><img class='big' src='{uil[showImageStandardBig]}' /></a>
				<h3>{uil[name]}</h3>
				<h4>{uil[dealTitle]}</h4>
				<p>{uil[dealinfo]}</p>
				<address>{uil[address]}</address>
			</li>'''
			tmp = tmp + currentObject.format(**locals())
		# Wraps it in the Unordered List
		ul = '''
			<ul>'''+tmp+'''
			</ul>
		'''
		# sets the .__ul 
		self.ul = ul