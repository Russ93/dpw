# Russell Schlup
# January 15, 2013
# DPW
import webapp2
from htm import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()
		self.response.write(page.head())
		self.response.write(page.form())
		self.response.write(page.foot())

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
