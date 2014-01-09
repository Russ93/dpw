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
		self.__form = '''
			<form method='GET'>
				<label>Username</label><input type='text' name='user' placeholder="Enter Your Desired Username" />
				<label>Password</label><input type='text' name='pass' placeholder="Enter Your Password" />
				<label>First Name</label><input type='text' name='fName' placeholder="Enter Your First Name" />
				<label>Last Name</label><input type='text' name='lName' placeholder="Enter Your Last Name" />
				<label>Email</label><input type='text' name='email' placeholder="Enter Your Email" />
				<button>Sign Up</button>
			</form>
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

	def form(self):
		return self.__form

	def foot(self):
		return self.__foot