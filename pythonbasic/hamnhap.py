print('hello word')
#end kết thúc bằng
print('hello everyone',end='|||')
#*objects
packing = 1,2,3
print('\n',packing)
#sep chia các phần tử bởi các ký tự điền vào
print('Dùng sep:')
print('hello','world','i am king!',sep='-')
#đọc file
print('Thao tác file:')
with open('hamnhap.txt','a+') as f:
	print('Hello world ! it is Python language',file=f)
	f.close()
with open('hamnhap.txt') as f:
	readfile=f.read()
	print(readfile)
	f.close()
#flush : giá trị mặc định là false 