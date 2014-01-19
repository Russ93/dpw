class Page():
#-------------------- initializer --------------------#
	def __init__(self):
		#-------------------- Head --------------------#		
		self.__header = '''
<!DOCTYPE>
<html>
	<head>
		<title>Countries</title>
		<link href='http://fonts.googleapis.com/css?family=Lato:300|Montserrat' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='css/c.css' />
	</head>
	<body>
		<div id="container">'''
		#-------------------- Buttons --------------------#
		self.__form='''
			<nav>
				<a href='/?animal=0'><button>Herp Seal</button></a>
				<a href='/?animal=1'><button>Arctic Fox</button></a>
				<a href='/?animal=2'><button>Arctic Ermine</button></a>
				<a href='/?animal=3'><button>Arctic Wolf</button></a>
				<a href='/?animal=4'><button>Arctic Hare</button></a>
			</nav>'''
		self.__tmp='''
			<h1>{obj.name}</h1>
			<ul>
				<li>
					<h3>Phylum:</h3>
					<p>{obj.phy}</p>
				</li>
				<li>
					<h3>Class:</h3>
					<p>{obj.classs}</p>
				</li>
				<li>
					<h3>Order:</h3>
					<p>{obj.order}</p>
				</li>
				<li>
					<h3>Family:</h3>
					<p>{obj.fam}</p>
				</li>
				<li>
					<h3>Genus:</h3>
					<p>{obj.gen}</p>
				</li>
				<li>
					<h3>Average Lifespan:</h3>
					<p>{obj.avg}</p>
				</li>
				<li>
					<h3>Habitat:</h3>
					<p>{obj.hab}</p>
				</li>
				<li>
					<h3>Geolocation:</h3>
					<p>{obj.geo}</p>
				</li>
				<li>
					<h3>What do they say?</h3>
					<p>{obj.say}</p>
				</li>
			</ul>
			<img src='{obj.img}' width='300px'/>
		'''
		#-------------------- Closers --------------------#
		self.__foot= '''
		</div>
	</body>
</html>'''
#-------------------- Returners --------------------#
	def head(self):
		return self.__header

	def form(self):
		return self.__form

	def tmp(self,obj):
		tmp = self.__tmp.format(**locals())
		return tmp
	def foot(self):
		return self.__foot