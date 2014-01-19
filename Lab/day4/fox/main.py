# Russell Schlup
# January 15, 2013
# DPW
import webapp2
from htm import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()

		self.response.write(page.head())
		if self.request.GET:
			a = int(self.request.GET['animal'])
			self.response.write(page.tmp(animals[a]))
		self.response.write(page.form())
		self.response.write(page.foot())

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
class Chordata(object):
	def __init__(self):
		self._phy = 'Chordata'
		self._say = ''
	@property
	def phy(self):
		return self._phy
	@property
	def avg(self):
		return self._avg
	@property
	def hab(self):
		return self._hab
	@property
	def geo(self):
		return self._geo
	@property
	def img(self):
		return self._img
	@property
	def say(self):
		return self._say

class Mammalia(Chordata):
	def __init__(self):
		Chordata.__init__(self)
		self._class = 'Mammalia'
	@property
	def classs(self):
		return self._class
