class SinhVien:
	"""docstring for SinhVien """
	def __init__(self,name,old,Class):
		self.name,self.old,self.Class = name,old,Class
	'''def GetName(self):
		return self.name
	def GetOld(sefl):
		return self.old
	def GetClass(self):
		return self.Class'''
		
class MonHoc(SinhVien):
	def __init__(self,name,old,Class,tenmh,sotinhchi,HocPhiMotTinhChi):
		super().__init__(name,old,Class)
		self.tenmh,self.sotinhchi,self.HocPhiMotTinhChi = tenmh,sotinhchi,HocPhiMotTinhChi
	'''def GetTenMH(self):
		return self.tenmh
	def GetSoTC(self):
		return self.sotinhchi
	def HPMTC(self):
		return self.HocPhiMotTinhChi
	'''
	def HocPhiMH(self):
		return self.sotinhchi * self.HocPhiMotTinhChi

	
SV = MonHoc('Nguyen van an',20,'DA17TT','Toan roi rac',3,350000)
print(SV.__dict__)
print('Học phí một môn học:',SV.HocPhiMH())		
