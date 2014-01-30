# Russell Schlup
# January 29, 2013
# DPW - Final
import webapp2
from htm import *
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	page = Page()


        self.response.write(page.head)
        self.response.write(page.nav)
        if self.request.GET:
        	view.template(model.do(self.request.GET['song']))
        	self.response.write(view.view)

        self.response.write(page.close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
