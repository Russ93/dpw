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

        self.response.write(page.close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
