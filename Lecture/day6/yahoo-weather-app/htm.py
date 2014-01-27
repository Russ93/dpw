import urllib2
from xml.dom import minidom
class WeatherView(object):
	def __init__(self, obj):
		self.__content = ''
		for a in obj.forecast:
			self.__content += '<div>'+a['day']+' : <br />'
			self.__content += '<img src="http://l.yimg.com/a/i/us/we/52/'+a['code']+'.gif"/><br />'
			self.__content += 'High: ' + a['high']+''
			self.__content += '- Low: ' + a['low'] +'</div>'
	@property
	def content(self):
		return self.__content
class Page(object):
#-------------------- initializer --------------------#
	def __init__(self):
		#-------------------- Head --------------------#		
		self.__header = '''
<!DOCTYPE>
<html>
	<head>
		<title>Age Calculator</title>
		<style>
			html{
			font-family: 'Lato', 'Avenir', Arial, Helvetica, sans-serif;
			}
			div{
			float: left;
			margin: 50px 0 0 50px;
			}
		</style>
	</head>
	<body>'''
		#-------------------- Closers --------------------#
		self.__foot= '''
	</body>
</html>'''
#-------------------- Returners --------------------#
	@property
	def head(self):
		return self.__header
	@property
	def foot(self):
		return self.__foot
class Form(Page):
	def __init__(self, obj):
		super(Form, self).__init__()
		self.method = 'GET'
		self.action = ''
		self.__formOpen = '''
		<form action='{self.action}' method='{self.method}' name='ageCalc'>'''
		self.__input = ''
		for el in obj:
			string = '''
			<input type='{el[type]}' value='{el[label]}' name='{el[name]}' />'''
			self.__input = self.__input + string.format(**locals())

		self.__formClose = '</form>'
	@property
	def getForm(self):
		return self.__formOpen + self.__input + self.__formClose
	def update(self):
		self.__formOpen = self.__formOpen.format(**locals())
class WeatherModel(object):
	''' Handle communication with yahoo api. sends zip and get's wather info in XML, processes the xml and sends data out'''
	#setup
	def __init__(self, zip):
		self.__url = 'http://xml.weather.yahoo.com/forecastrss?p=' #url we are going to load the page from
		self.__req = urllib2.Request(self.__url + zip) # concat zip with url
		self.__opener = urllib2.build_opener() #magic to load request creates framework to get url
		self.__do = WeatherData()
		self.send()

	#sends data
	def send(self):
		self.__result = self.__opener.open(self.__req) #gets url and puts result in 'result'
		self.sort()
	#recieve data
	#sort data
	def sort(self):
		self.__xmldoc = minidom.parse(self.__result) #parse through string to get XML object
		self.__do.title = self.__xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue
		fList = self.__xmldoc.getElementsByTagName('yweather:forecast')
		for l in fList:
			tmp = dict()
			tmp['day'] = l.attributes['day'].value
			tmp['code'] = l.attributes['code'].value
			tmp['high'] = l.attributes['high'].value
			tmp['low'] = l.attributes['low'].value
			self.__do.forecast.append(tmp) #pushes info into the array
		#title
		#forecast - day, high, low, code
	@property
	def do(self):
		return self.__do

class WeatherData(object):
	def __init__(self):
		self.title = '' #public
		self.forecast = []