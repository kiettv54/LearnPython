class Student(object):
	"""docstring for Student"""
	def __init__(self, name, old,Class):
		self.name,self.old,self.Class = name,old,Class
	def GetName(sefl):
		return sefl.name
	def GetOld(sefl):
		return sefl.old
	def GetClass(sefl):
		return sefl.Class
	def __del__(sefl):
		del sefl.name,sefl.old,sefl.Class
St = Student('Nguyen van a',18,'Da17TT')
print(St.GetName())
print(St.GetOld())
print(St.GetClass())
		
		