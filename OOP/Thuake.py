class Student(object):
	"""docstring for Student"""
	def __init__(self, name, old,Class):
		self.name,self.old,self.Class = name,old,Class
	def GetName(self):
		return self.name
	def GetOld(self):
		return self.old
	def GetClass(self):
		return self.Class
	def __del__(self):
		del self.name,self.old,self.Class

class Math(Student):
	def __init__(self, name,old,Class, toan ,ly ,hoa):
		super().__init__(name,old,Class)
		self.toan,self.ly,self.hoa = toan,ly,hoa
	def GetToan(self):
		return self.toan
	def GetLy(self):
		return self.ly
	def GetHoa(self):
		return self.hoa
	def __del__(self):
		del self.toan,self.ly,self.hoa
sv = Math('Nguyễn An',19,'Da17TT',7,8,9)
print(sv.GetName(),sv.GetOld(),sv.GetClass(),sv.GetToan(),sv.GetLy(),sv.GetHoa())
