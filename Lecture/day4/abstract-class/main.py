# Russell Schlup
# January 15, 2013
# DPW
import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = FormPage()
		page.title = 'herp a derp!'
		page.css = '<link href="c/c.css" rel="stylesheet" type="text/css" />'
		page.update()
		self.response.write(page.head)
		self.response.write(page.getForm)
		self.response.write(page.close)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)

class PageBase(object):
	def __init__(self):
		self.title = 'welcome to your doom!'
		self.css = '<link href="c/c.css" rel="stylesheet" type="text/css" />'
		self._head = '''
<!DOCTYPE>
<html>
	<head>
		<title>{self.title}</title>
		{self.css}
	</head>
	<body>'''
		self.__foot = '''
	</body>
</html>'''
	@property
	def head(self):
		return self._head

	@property
	def close(self):
		return self.__foot

	def update(self):
		self.__head = self.__head.format(**locals())
class FormPage(PageBase):
	def __init__(self):
		super(FormPage, self).__init__() #calling PageBase's init funciton
		self.method = 'GET'
		self.action = ''
		self.__formOpen = '''
		<form action='{self.action}' method='{self.method}' name='ageCalc'>
			<label>Enter your year of birth</label>
			<input type='text' name='yearBorn' size='5' autofocus='autofocus'/>
			<button>Enter</button>
		'''
		self.__formClose = '''
		</form>
		'''
	@property
	def getForm(self):
		return self.__formOpen + self.__formClose

	def update(self):
		self._head = self._head.format(**locals())
		self.__formOpen = self.__formOpen.format(**locals())