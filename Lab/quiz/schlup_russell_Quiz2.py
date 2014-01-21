class Car(object):
	def __init__(self):
		self._year = '1993'
		self.__make = 'Ford'
		self.__model = 'Taurus'
	@property
	def year(self):
		return self._year
	@property
	def make(self):
		return self.__make
	@property
	def model(self):
		self.__model

class update(Car):
	def __init__(self):
		Car.__init__(self)
		super(Car, self).__init__()

	@property
	def year(self):
		return self._year
	@year.setter
	def year(self,year):
		self._year = year

#----- Initiates
update = update()
#----- Use this to set the year
update.year = '2001'
#----- Print
print update.year