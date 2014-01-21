# Russell Schlup
# January 20, 2013
# DPW
import webapp2
from htm import *
import urllib2
from xml.dom import minidom #library for working with xml

class MainHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.GET:
			zip = self.request.GET['zip'] #takes zip from url and stores it
			url = 'http://xml.weather.yahoo.com/forecastrss?p=' #url we are going to load the page from
			req = urllib2.Request(url + zip) # concat zip with url
			opener = urllib2.build_opener() #magic to load request creates framework to get url
			result = opener.open(req) #gets url and puts result in 'result'
			xmldoc = minidom.parse(result) #parse through string to get XML object
			content = ''
			fList = xmldoc.getElementsByTagName('yweather:forecast')
			for l in fList:
				content += l.attributes['day'].value+' : <br />'
				content += '<img src="http://l.yimg.com/a/i/us/we/52/'+l.attributes['code'].value+'.gif"/>'
				content += 'High: ' + l.attributes['high'].value +'<br />'
				content += '- Low: ' + l.attributes['low'].value +'<br />'


		form_settings = [{'name':'zip', 'type':'text', 'label':'Enter your zip code'},
						 {'name':'submit', 'type':'submit', 'label':'Get Weather'}]
		page = Page()
		form = Form(form_settings)

		form.update()
		self.response.write(form.head)
		self.response.write(form.getForm)
		self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
		self.response.write(content)
		#self.response.write(xmldoc.getElementsByTagName('description')[1].firstChild.nodeValue)
		self.response.write(form.foot)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
