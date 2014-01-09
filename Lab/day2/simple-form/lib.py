class Page():
#-------------------- initializer --------------------#
	def __init__(self):
		self.__header = '''
<!DOCTYPE>
<html>
	<head>
		<title>{title}</title>
		<link rel='stylesheet' href='css/c.css' />
	</head>
	<body>
			'''
		self.__body = '''
		<nav>
			<ul>
				<li><img src="i/l.png" id="logo"/></li>
				<li>Login</li>
			</ul>
		</nav>
		<section id="cta">
			<h1>Start Remembering</h1>
			<p>This app will make modern note taking obsolete and make modern life a bit more manageable by  allowing to take note of everything and never lose information</p>
			<span>Create a free account</span>
		'''

		self.__foot= '''
		</section>
	</body>
</html>
			'''
#-------------------- html returns --------------------#
	def head(self, title):
		header = self.__header.format(**locals())
		return header

	def body(self):
		return self.__body


	def foot(self):
		return self.__foot