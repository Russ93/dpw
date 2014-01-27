class Person(object):
	def __init__(self):
		self.name = 'joe'
		self.age = 15
		self.height = 6
		self.weight = 159

nicole = Person()
nicole.name = 'Nicole'
nicole.height = 12

russell = Person()
russell.name = 'russell'
russell.height = 7

print nicole.height
print russell.height