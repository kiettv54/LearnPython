class SieuNhan:
	"""docstring for SieuNhan"""
	suc_manh =50
	def __init__(self, name, vukhi,mausac):
		self.name,self.vukhi,self.mausac = name,vukhi,mausac
	@classmethod
	def fromstring(self, s):
		lis = s.split('-')
		new_list = [st.strip() for st in lis]
		ten,vukhi,mausac = new_list
		return self(ten,vukhi,mausac)
strs ='do-kiem-do'
sn = SieuNhan.fromstring(strs)
print(sn.__dict__)

