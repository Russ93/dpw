# Russell Schlup
# January 13, 2013
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	luke = Character(5555)
    	luke.name = 'Luke Skywalker'
    	luke.age = 20
    	luke.rank = 'Jedi'

    	leia = Character(1234)
    	leia.name = 'Leia Skywalker'
    	leia.age = luke.age
    	leia.rank = 'Princess'

    	han = Character(666)
    	han.name = 'Han Solo'
    	han.age = 29
    	han.rank = 'Smuggler'

    	heroes = [luke,leia,han]

    	for h in heroes:
        	self.response.write('<p>'+h.name+'</p>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

class Character(object):
	def __init__(self, pin):
		self.name = ''
		self.age = 0
		self.rank = ''
		self.__password = pin #read only private variable
	@property
	def password(self):
		return self.__password