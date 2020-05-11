so_list = []
so = 1
while len(so_list) < 5:
	if so % 2 == 0:
		so_list.append(so)
	so += 1
print(so_list)
d='troll'
x=0
while x < len(d):
	print(x,d[x])
	x+=1
#contineu
x = 0
a = []
while True:
	x += 1
	if x % 2 == 0:
		continue
	a.append(x)
	if len(a) == 5:
		break
print(a)
a = [56,14,11,756,34,90,11,11,65,0,11,35]
b = a.copy()
while a.count(11)>0: #xóa bỏ số 11 trong list

	a.remove(11)
a.sort() #sắp xếp các số
idx = 0
while idx < len(b): #thêm 11 vào các vị trí đúng của nó
	if b[idx] == 11:
		a.insert(idx,11)
	idx += 1
print(a)

fileopen = open('braft.txt',mode = 'r+')
fileopen2 = open ('Kteam.txt',mode = 'w+')
data = fileopen.readline()
while data != '':
	data_str = data.split()
	dem = 2
	while dem < len(data_str):
		if data_str[dem -1] == 'Kteam':
			data_str[dem -2] = 'How'
		fileopen2.write(data_str[dem -2] + ' ')
		dem += 1
	fileopen2.write(data_str[dem -2] +'\n')
	data = fileopen.readline()	
fileopen.close()
print(fileopen2.read())
fileopen2.close()

lenth = 5
arr = (x for x in range(lenth))

c=0
while c < lenth:
	#print(next(arr))
	#c +=1
	try:
		print(next(arr))
		c += 1
	except StopIteration:
		break