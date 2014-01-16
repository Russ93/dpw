# Russell Schlup
# January 15, 2013
# DPW
# Quiz 1: Basic Python syntax
class main(object):
	def __init__(self):
		str = ''
	def calcArea(self,height,width):
		area = height*width
		if height == width:
			str = 'Square'
		else:
			str='Rectangle'
		ret = '''Your {str}'s area is {area}'''
		ret = ret.format(**locals())
		return ret
	def countDown(self,num):
		for i in range(0,num):
			num1 = num - 1
			str = '''{num} Bottles of Beer on the Wall, {num} Bottles of Beer.. take one down and pass it around. Now you have {num1} bottles of beer on the wall!'''
			str = str.format(**locals())
			num = num1
			print str

m = main()	
print m.calcArea(5,5)
print m.calcArea(4,5)
m.countDown(100)