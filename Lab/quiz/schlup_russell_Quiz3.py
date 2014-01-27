class BigAnswer(object):
	def __init__(self):
		self._answer = 42
		self.comb = '''Question: {self.question}
Answer: {self.answer}'''

	@property
	def answer(self):
		return self._answer

	@property
	def combine(self):
		self.comb = self.comb.format(**locals())
		return self.comb

class FirstQuestion(BigAnswer):
	def __init__(self):
		super(BigAnswer, self).__init__()
		BigAnswer.__init__(self)
		self.__question = 'What is the answer to life the universe and everything?'

	@property
	def question(self):
		return self.__question

class BetterQuestion(FirstQuestion):
	def __init__(self):
		super(FirstQuestion, self).__init__()
		FirstQuestion.__init__(self)
		self._newQuestion = 'How many roads must a man walk down?'

	@property
	def question(self):
		return self._newQuestion

fq = FirstQuestion()
bq = BetterQuestion()
print fq.combine
print bq.combine