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

#-------------------- html returns --------------------#
	def head(self, title):
		header = self.__header.format(**locals())
		return header
