#bài 1
def GiaiThua(x):
	x = abs(x)
	if x == 0 or x == 1 : return 1
	else:
		return x*GiaiThua(x-1)
n = 6
print(n,'!= ',GiaiThua(n))
d = dict()
for x in range(1,n-1):
	d[x] = x*x
print(d)
#bài 2
values = '34,35,36,37,38'#input('Enter string number:')
l = values.split(',')
t = tuple(l)
print(l)
print(t)
#bài 3
class InputUpperString(object):
	"""docstringIn
	putUpperString"""
	def __init__(self):
		self.s = ''
	def GetString(self):
		self.s = 'anhyeuem'#str(input('Enter String:'))
	def PrintString(self):
		ss = self.s.upper()
		print('String after Uppering:',ss)
IP = InputUpperString()
IP.GetString()
IP.PrintString()
n = 4
def BinhPhuong(x):
	return x ** 2
print(BinhPhuong(3))
n = '3,5'#str(input("Enter X,Y:"))

item = [int(x) for x in n.split(',')]
row = item[0]
colunm = item[1]
multilist = [[0 for value in range(colunm)] for value2 in range(row) ]
for i in range(row):
	for j in range(colunm):
		multilist[i][j] =i*j
print(multilist)