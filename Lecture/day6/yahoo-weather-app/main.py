# Russell Schlup
# January 20, 2013
# DPW
import webapp2
from htm import *
import urllib2
from xml.dom import minidom #library for working with xml

class MainHandler(webapp2.RequestHandler):
	'''
		Main Controller for the weather application
	'''
	def get(self):
		form_settings = [{'name':'zip', 'type':'text', 'label':'Enter your zip code'},
						 {'name':'submit', 'type':'submit', 'label':'Get Weather'}]
		page = Page()
		form = Form(form_settings)

		form.update()

		self.response.write(form.head)
		self.response.write(form.getForm)
		if self.request.GET:
			wModel = WeatherModel(self.request.GET['zip'])
			data = wModel.do
			print data
			wView = WeatherView(data)
			self.response.write(wView.content)

		self.response.write(form.foot)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
