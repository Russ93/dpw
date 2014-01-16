class Page():
#-------------------- initializer --------------------#
	def __init__(self):
		#-------------------- Head --------------------#		
		self.__header = '''
<!DOCTYPE>
<html>
	<head>
		<title>Countries</title>
		<link href='http://fonts.googleapis.com/css?family=Lato:300|Josefin+Slab:300' rel='stylesheet' type='text/css'>
		<link rel='stylesheet' href='css/c.css' />
	</head>
	<body>
		<div id="container">
			'''
		#-------------------- Buttons --------------------#
		self.__form='''
	 		<form>
				<input type='text' name='button' value='1' /><button>Asia</button>
			</form>
			<form>
				<input type='text' name='button' value='2' /><button>Africa</button>
			</form>
			<form>
				<input type="text" name="button" value="3" /><button>Europe</button>
			</form>
			<form>
				<input type="text" name="button" value="4" /><button>Latin America</button>
			</form>
			<form>
				<input type="text" name="button" value="5" /><button>North America</button>
			</form>
			<form>
				<input type="text" name="button" value="6" /><button>Oceania</button>
			</form>
			<form>
				<input type="text" name="button" value="0" /><button>World</button>
			</form>
			'''
		#-------------------- Closers --------------------#
		self.__foot= '''
		</div>
	</body>
</html>
			'''
#-------------------- Returners --------------------#
	def head(self):
		return self.__header

	def form(self):
		return self.__form

	def foot(self):
		return self.__foot