class Page():
#-------------------- initializer --------------------#
	def __init__(self):
		self.__header = '''
<!DOCTYPE>
<html>
	<head>
		<title>{title}</title>
		<link href='http://fonts.googleapis.com/css?family=Lato:300|Josefin+Slab:300' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='css/n.css' />
		<link rel='stylesheet' href='css/c.css' />
	</head>
	<body>
			'''
		self.__body = '''
		<nav>
			<ul>
				<li><img src="css/l.png" id="logo"/></li>
				<li>Login</li>
			</ul>
		</nav>
		<section id="cta">
		'''
		self.__regis = '''
			<h1>Start Remembering</h1>
			<p>This app will make modern note taking obsolete and make modern life a bit more manageable by  allowing to take note of everything and never lose information</p>
			<span>Create a free account</span>
			<form method='GET'>
				<label>username</label><input type='text' name='user' placeholder="Enter Your Desired Username" />
				<label>password</label><input name='pass' type='password' placeholder="Enter Your Password" />
				<label>first name</label><input type='text' name='fName' placeholder="Enter Your First Name" />
				<label>last name</label><input type='text' name='lName' placeholder="Enter Your Last Name" />
				<label>email</label><input type='text' name='email' placeholder="Enter Your Email" />
				<label></label><button>Sign Up</button>
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

	def regis(self):
		return self.__regis

	def foot(self):
		return self.__foot