import urllib2
from xml.dom import minidom
class Page(object):
	def __init__(self):
		self.__header = '''
<!doctype html>
<html>
<head>
	<title>iTunes Music</title>
	<style>html{font-family: Helvetica;}nav{float: left;}article img{float: left;}article{float: left; margin-left: 25px;}article ul{float: left;}</style>
</head>
<body>
		'''
		self.__nav = '''
	<nav>
		<ul>'''
		self.__body = '''
	<h1>Hello World</h1>
		'''
		self.__close = '''
</body>
</html>
		'''
	@property
	def head(self):
		return self.__header

	@property
	def body(self):
		return self.__body
	@body.setter
	def body(self,val):
		self.__body = val

	@property
	def close(self):
		return self.__close

	@property
	def nav(self):
		return self.__nav
	@nav.setter
	def nav(self,li):
		for i in li:
			self.__nav = self.__nav + '<li><a href="/?song='+i+'">'+i+'</a></li>'
		self.__nav = self.__nav + '</ul></nav>'

class View(object):
	def __init__(self):
		self.__view = ''

	@property
	def view(self):
		return self.__view

	def template(self, obj):
		print obj
		strang = '''
		<article>
			<img src='covers/{obj[cover]}' />
			<ul>
				<li>{obj[title]}</li>
				<li>{obj[length]}</li>
				<li>{obj[artist]}</li>
				<li>{obj[length]}</li>
				<li>{obj[year]}</li>
			</ul>
		</article>'''
	#		<audio controls>
	#			<source src='mp3s/{obj[mp3]}' type='audio/mpeg'/>
	#		</audio>
		strang = strang.format(**locals())
		self.__view = strang