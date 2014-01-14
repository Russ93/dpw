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

		africa = Region()
		africa.name = 'Africa'
		africa.population = 1110635062
		africa.area = 30955880

		europe = Region()
		europe.name = 'Europe'
		europe.population = 742452170
		europe.area = 23048931

		latinAmerica = Region()
		latinAmerica.name = 'Latin America and Caribbean'
		latinAmerica.population = 616644503
		latinAmerica.area = 20546598

		northAmerica = Region()
		northAmerica.name = 'Northern America'
		northAmerica.population = 355360791
		northAmerica.area = 21775893

		oceania = Region()
		oceania.name = 'Oceania'
		oceania.population = 38303620
		oceania.area = 8563295

		world = Region()
		world.name = 'Earth'
		world.population = 7162119434
		world.area = 136806988

		areas = [world,asia,africa,europe,latinAmerica,northAmerica,oceania]

		if self.request.GET:
			button = int(self.request.GET['button'])
			self.response.write(self.html(areas[button]))

		self.response.write(page.form())
		self.response.write(page.foot())
	def html(self,obj):
		percent =obj.population*100/obj.world
		dens =obj.population/obj.area
		stranged = '''
		<h1>{obj.name}</h1>
		<ul>
			<li>
				<h3>2013 Population</h3>
				<p>{obj.population}</p>
			</li>
			<li>
				<h3>Percent of World Pop.</h3>
				<p>{percent}%</p>
			</li>
			<li>
				<h3>Area (km 2)</h3>
				<p>{obj.area}</p>
			</li>
			<li>
				<h3>Density (Population/km 2)</h3>
				<p>{dens}</p>
			</li>
		</ul>
		'''
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
		