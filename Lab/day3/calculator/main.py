# Russell Schlup
# January 13, 2013
# DPW
import webapp2
from htm import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		#----- pull the page class html from the html.py
		page = Page()

		#----- head of the html -----#
		self.response.write(page.head())

		#----- Asia -----#
		asia = Region()
		asia.name = 'Asia'
		asia.population = 4298723288
		asia.area = 31915446

		#----- Africa -----#
		africa = Region()
		africa.name = 'Africa'
		africa.population = 1110635062
		africa.area = 30955880

		#----- Europe -----#
		europe = Region()
		europe.name = 'Europe'
		europe.population = 742452170
		europe.area = 23048931

		#----- Latin America -----#
		latinAmerica = Region()
		latinAmerica.name = 'Latin America and Caribbean'
		latinAmerica.population = 616644503
		latinAmerica.area = 20546598

		#----- North America -----#
		northAmerica = Region()
		northAmerica.name = 'Northern America'
		northAmerica.population = 355360791
		northAmerica.area = 21775893

		#----- Everything Else XD -----#
		oceania = Region()
		oceania.name = 'Oceania'
		oceania.population = 38303620
		oceania.area = 8563295

		#----- All Together Now! -----#
		world = Region()
		world.name = 'Earth'
		world.population = 7162119434
		world.area = 136806988

		#----- Hold all of the region objects -----#
		areas = [world,asia,africa,europe,latinAmerica,northAmerica,oceania]

		#----- If something is clicked then display what was clicked
		#----- Using the number attached to each button it will call
		#----- The correct item from the array
		if self.request.GET:
			button = int(self.request.GET['button'])
			self.response.write(self.html(areas[button]))

		#----- HTML BUTTONS -----#
		self.response.write(page.form())
		#----- HTML Closer -----#
		self.response.write(page.foot())
	#--------------- Html formatter for the objects returned ---------------#
	def html(self,obj):
		#----- takes the float of every number as to get an actual decimal
		#----- the "%.2f" shows only 2 decimal places instead of the whole thing 
		percent = "%.2f" % float(float(obj.population*100)/float(obj.world))
		dens = "%.2f" % float(float(obj.population)/float(obj.area))
		#----- This is the string format for the html		
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
		#----- formats the string
		stranged = stranged.format(**locals())
		#----- then returns the string to go into 
		#----- the response.write on line 65
		return stranged
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

#--------------- Data Objects ---------------#
class Region(object):
	def __init__(self):
		self.name = ''
		self.__population = 0
		self.area = 0
		self.world = 7162119434
	#----- Getter for population
	@property
	def population(self):
		return self.__population
	#----- Setter for population
	@population.setter
	def population(self, value):
		self.__population = value
		