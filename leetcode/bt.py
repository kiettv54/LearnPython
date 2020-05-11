import math
value = []
a ='100,150,180'.split(',')  #[x for x in input('Nhap chuoi so:').split(',')]
C = 50
H = 30
for value1 in range(len(a)):
	Q = str(int(round(math.sqrt((2 * C * float(a[value1]))/H))))
	value.append(Q)
print(value)
num = '3,5'.split(',')
row = int(num[0])
colum = int(num[1])
value = [[0 for l in range(colum)] for r in range(row) ]
for r in range(row):
	for l in range(colum):
		value[r][l] = r *l
print(value) 
string = 'without,hello,bag,world'.split(',')
string.sort()
print(','.join(string))
