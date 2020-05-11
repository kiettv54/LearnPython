class Test(object):
	"""docstring for Test"""
	def SumNumber(self,a):
		s = 0
		for value in range(len(a)):
			s += a[value]
		return s
arr = [1,2,3,4,5,6]
print(Test.SumNumber(arr))

