# Russell Schlup
# January 13, 2013
# DPW
import webapp2
from htm import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = Page()

		self.response.write(page.head())
		asia = Region()
		asia.name = 'Asia'
		asia.population = 4298723288
		asia.area = 31915446

		world = Region()
		world.name = 'Earth'
		world.population = 7162119434
		world.area = 136806988

		areas = [world,asia]

		if self.request.GET:
			button = int(self.request.GET['button'])
			self.response.write(self.html(areas[button]))

		self.response.write(page.form())
		self.response.write(page.foot())
		stranged = stranged.format(**locals())
		return stranged
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
class Region(object):
	def __init__(self):
		self.name = ''
		self.__population = 0
		self.area = 0
		self.world = 7162119434

	@property
	def population(self):
		return self.__population
	@population.setter
	def population(self, value):
		self.__population = value
		