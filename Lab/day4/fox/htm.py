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

		#-------------------- Closers --------------------#
		self.__foot= '''
		</div>
	</body>
</html>'''