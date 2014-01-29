# Russell Schlup
# January 24, 2013
# DPW
# API

import webapp2
from htm import *
import urllib2
import json #library for working with xml

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello World')

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
