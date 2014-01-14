# Russell Benton
# January 13, 2013
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        atm = ATM()
        #calling getter function
        #treats the funciton like a variable
        atm.account_number = 555
        self.response.write(atm.account_number)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

#for getters and setters to work
#you must have the class inherit from the object class
#always include object in the paranthesis
class ATM(object):
	def __init__(self):
		#private attributes/properties
		# two underscores = privates
		# one underscore = protected
		self.__account_number = 12345678

	#----- Getter Function -----#
	#  getters.... no underscore
	# no underscores = public
	@property
	def account_number(self):
		return self.__account_number
	#----- Setter Function -----#
	@account_number.setter
	def account_number(self, val):
		#check number of digits
		str_value = str(val) #converts to string
		length = len(str_value) #counts numer of chars in string
		if length == 8:
			self.__account_number = val
		else:
			print 'Error! Account number is no the right length'
