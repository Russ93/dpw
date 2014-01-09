#!/usr/bin/env python
#
# Russell Schlup
# January 9, 2013
# DWP

import webapp2
from lib import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	page = Page() #creates an instance of the imported page

    	title = 'Russell'
        self.response.write(page.head(title))

        self.response.write(page.foot())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
