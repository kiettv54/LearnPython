n = int(input('Nhap so luong phan tu:'))
a = []
while len(a) < n:
	k = int(input('Nhap a[' +str(len(a))+'] = '))
	a.append(k)
b = filter(lambda x:x%2,a)
print(list(b))
