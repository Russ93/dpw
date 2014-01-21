class Page(object):
#-------------------- initializer --------------------#
	def __init__(self):
		#-------------------- Head --------------------#		
		self.__header = '''
<!DOCTYPE>
<html>
	<head>
		<title>Age Calculator</title>
	</head>
	<body>'''
		#-------------------- Closers --------------------#
		self.__foot= '''
	</body>
</html>'''
#-------------------- Returners --------------------#
	@property
	def head(self):
		return self.__header
	@property
	def foot(self):
		return self.__foot
class Form(Page):
	def __init__(self, obj):
		super(Form, self).__init__()
		self.method = 'GET'
		self.action = ''
		self.__formOpen = '''
		<form action='{self.action}' method='{self.method}' name='ageCalc'>'''
		self.__input = ''
		for el in obj:
			string = '''
			<input type='{el[type]}' value='{el[label]}' name='{el[name]}' />'''
			self.__input = self.__input + string.format(**locals())

		self.__formClose = '</form>'
	@property
	def getForm(self):
		return self.__formOpen + self.__input + self.__formClose
	def update(self):
		self.__formOpen = self.__formOpen.format(**locals())