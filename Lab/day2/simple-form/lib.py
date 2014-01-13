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
		self.__pre = '''
		<h1>Congrtulations {submit[first]},{submit[last]}</h1>
		<p>You have signed up for Written online note taker sadly this site isn't completely set up ,but thank you for showing your appreciation by signing up early, we greatly appreciate it!</p>
		<strong>Below is the information you will use to sign in with.</strong>
		<ul>'''
		self.__regis = '''
			<h1>Start Remembering</h1>
			<p>This app will make modern note taking obsolete and make modern life a bit more manageable by  allowing to take note of everything and never lose information</p>
			<span>Create a free account</span>
			<form method='GET'>
				<label>username</label><input type='text' name='username' placeholder="Enter Your Desired Username" />
				<label>password</label><input name='pass' type='password' placeholder="Enter Your Password" />
				<label>first name</label><input type='text' name='first' placeholder="Enter Your First Name" />
				<label>last name</label><input type='text' name='last' placeholder="Enter Your Last Name" />
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
	def returnedSub(self, submit):
		returned = self.__pre
		#----- prefix the html -----#
		for key in submit:
#		----- for loops thorugh the object returned -----		#
			pull = submit[key]
			#----- pulls the item out of the object with the current key
			returned = returned+'''
            <li>
				<h2>'''+key+''':</h2>
				<p>'''+pull+'''</p>
			</li>'''
			#----- make the key into an H2 and the pulled item into a paragraph
		returned = returned+'''
		</ul>'''
		#----- finishes off the ul
		returned = returned.format(**locals())
		return returned