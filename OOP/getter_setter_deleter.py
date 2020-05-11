
class Person(object):
	"""docstring for Person"""
	def __init__(self, ho,ten,tuoi,std):
		self.ho,self.ten,self.tuoi,self.std = ho,ten,tuoi,std
	#getter
	@property
	def Hoten(self):

		return '{} {}'.format(self.ho,self.ten)
	#getter
	@property
	def email(self):
		b = self.ho +self.ten
		b = b.split(' ')
		b.append('@gmail.com')
		d = ''
		for x in range(len(b)):
			d += b[x]
		return d
	#setter
	@Hoten.setter
	def Hoten(self,new_name):
		new_ho,new_name = new_name.split(' ')
		self.ho,self.ten = new_ho,new_name
	#deleter
	@Hoten.deleter
	def Hoten(self):
		self.ho = None
		self.ten = None
		print('Đã xóa')
ps = Person('nguyen','thien an',18,'0901074682')
ps.Hoten = 'Hong Anh'
print(ps.Hoten)
print(ps.tuoi)
print(ps.std)
print(ps.email)
del ps.Hoten
print(ps.Hoten)
