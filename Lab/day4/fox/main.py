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
#----- Herbavoures -----#
class Lagomorpha(Mammalia):
	def __init__(self):
		Mammalia.__init__(self)
		self._order = 'Lagomorpha'
	@property
	def order(self):
		return self._order

#----- Carnivoures -----#
class Carnivora(Mammalia):
	def __init__(self):
		Mammalia.__init__(self)
		self._order = 'Carnivora'
	@property
	def order(self):
		return self._order

#----- Seal -----#
class Phocidae(Carnivora):
	def __init__(self):
		Carnivora.__init__(self)
		self._fam = 'Phocidae'
	@property
	def fam(self):
		return self._fam
class Pagophilus(Phocidae):
	def __init__(self):
		Phocidae.__init__(self)
		self._say = 'ARR ARR ARR'
		self._genus = 'Pagophilus'
		self._avg = '20 to 35 years'
		self._hab = 'saltwater or marine'
		self._geo = 'polar'
		self._img = 'http://www.scenicreflections.com/files/Cute_Harp_Seal_Wallpaper_ymwg1.jpg'
	@property
	def gen(self):
		return self._genus

#----- Fox -----#
class Canidae(Carnivora):
	def __init__(self):
		Carnivora.__init__(self)
		self._fam = 'Canidae'
	@property
	def fam(self):
		return self._fam
class Vulpes(Canidae):
	def __init__(self):
		Canidae.__init__(self)
		self._say = 'Ya cha cha cha cha cha chow'
		self._genus = 'Vulpes'
		self._avg = '16.3 years'
		self._hab = 'tundra'
		self._geo = 'polar'
		self._img = 'http://www.animalhdwallpapers.com/wp-content/uploads/wallpapers/Foxes/Arctic-Fox-in-Snow-Wallpaper.jpg'
	@property
	def gen(self):
		return self._genus

#----- Ermine (ferret) -----#
class Mustelidae(Carnivora):
	def __init__(self):
		Carnivora.__init__(self)
		self._fam = 'Mustelidae'
	@property
	def fam(self):
		return self._fam
class Mustela(Mustelidae):
	def __init__(self):
		Mustelidae.__init__(self)
		self._say = 'aaahh eekk eekk'
		self._genus = 'Mustela'
		self._avg = '12.5 (high) years'
		self._hab = 'tundra'
		self._geo = 'polar'
		self._img = 'http://media.tumblr.com/tumblr_m5vth5mrY21ros5rk.png'
	@property
	def gen(self):
		return self._genus

#----- Wolf -----#
class Canis(Canidae):
	def __init__(self):
		Canidae.__init__(self)
		self._say = 'arrwoooo'
		self._genus = 'Canis'
		self._avg = '12.5 (high) years'
		self._hab = 'tundra'
		self._geo = 'polar'
		self._img = 'http://www.robertwinslowphoto.com/Animals/North-and-South-American/Wolf-Arctic/Arctic-Wolf-BF-09W8C/111249704_xjUNn-L.jpg'
	@property
	def gen(self):
		return self._genus

#----- Bunny -----#
class Leporidae(Lagomorpha):
	def __init__(self):
		Lagomorpha.__init__(self)
		self._fam = 'Leporidae'
	@property
	def fam(self):
		return self._fam
class Lepus(Leporidae):
	def __init__(self):
		Leporidae.__init__(self)
		self._say = 'ntch ntch ntch'
		self._genus = 'Lepus'
		self._avg = '3 to 5 years'
		self._hab = 'tundra'
		self._geo = 'polar'
		self._img = 'http://www.waynelynch.ca/arctic_gallery/8-Arctic_Hare_101.jpg'
	@property
	def gen(self):
		return self._genus