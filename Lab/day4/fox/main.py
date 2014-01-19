# Russell Schlup
# January 15, 2013
# DPW
import webapp2
from htm import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello World')

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
