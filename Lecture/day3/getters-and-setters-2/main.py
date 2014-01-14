#Russell Schlup
#january 13, 2013

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	russell = Transscript()
    	russell.grade1 = 20
    	#list the grades
    	#calculate the averages
    	#show the average
        self.response.write(russell.print_num())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
class Transscript(object):
	def __init__(self):
		#attributes - that are private - should have underscores - convention - tradition
		self.__grade1 = 90
		self.__grades = [self.__grade1,80,60]
	@property
	def grade1(self): #convention - don't have underscores... just tradition
		pass
#		#this is what tells computer to associate grade1 with __grade1
#		return self.__grade1
	@grade1.setter
	def grade1(self, value):
		self.__grade1 = value
		return self.__grade1
	def calc_average(self):
		sum = 0
		for g in self.__grades:
			sum = g+sum
		avg = sum/len(self.__grades)
		return avg
	def print_num(self):
		return self.__grade1