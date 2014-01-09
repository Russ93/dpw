#!/usr/bin/env python
#
# Russell Schlup
# DPW
# 1/8/14
import webapp2

from lib import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
		#self.response.write('Hello world!')
		#calling the method "click".. which returns fills lbl
#		button = Button()
		#printing out lbl
#		lbl = button.label
#		self.response.write(button.label)
		
		page = Page() #creates an instance of the imported page
		
#		title = "Welcome!"
		self.response.write(page.open())
		
#		p = p.format(**locals())
		
		if self.request.GET:
			self.response.write(self.request.GET['login'])
		else:
			form = '''
			<form method='GET'>
				<label>login</label><input type='text' name='login' />
				<label>email</label><input type='text' name='email' />
				<button>Submit</button>
			</form>
			'''
		
#		self.response.write(p)
			self.response.write(form)
		self.response.write(page.close())
#class Button():
#	
#	def __init__(self):
#		self.label = 'Contact us'
#	
#	@property #decorator
#	def label(self):
#		return self.__label
#		
#	@label.setter #setter decorator
#	def label(self, l):
#		self.__label = l
#	
#	def label(self):
#		return self.label



app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
