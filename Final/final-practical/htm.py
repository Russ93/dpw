import urllib2
from xml.dom import minidom

class Model(object):
	def __init__(self):	
		self.__xmldoc = minidom.parse(open('Music.xml', 'r'))
		self.__tracks = self.__xmldoc.getElementsByTagName('track')
		#print self.__tracks
		self.__tracksArr = []
		self.__titles = []
		for t in self.__tracks:
			track = dict()
			track['title'] = t.getElementsByTagName('title')[0].firstChild.nodeValue
			track['artist'] = t.getElementsByTagName('artist')[0].firstChild.nodeValue
			track['length'] = t.getElementsByTagName('length')[0].firstChild.nodeValue
			track['year'] = t.getElementsByTagName('year')[0].firstChild.nodeValue
			track['label'] = t.getElementsByTagName('label')[0].firstChild.nodeValue
			track['cover'] = t.getElementsByTagName('cover')[0].firstChild.nodeValue
			self.__tracksArr.append(track)
			self.__titles.append(track['title'])
	def do(self, name):
		for t in self.__tracksArr:
			if t['title'] == name:
				return t
	@property
	def lis(self):
		return self.__titles
class Page(object):
	def __init__(self):
		self.__header = '''
<!doctype html>
<html>
<head>
	<title>iTunes Music</title>
	
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