def test(a,b,c):
	print(a)
	print(b)
	print(c)
lis = ['123','Hello mother fucker','laugth out loud']
#lưu ý khi sử dụng với key word
print(test(*lis))
#example using key word
def test2(k,t,e,*d):
	print(k)
	print(t)
	print(e)
	print('end',d)
lis2 = ['Surprise!','Hello mother fucker','laugh out loud']
test2(*lis2,'IQ infinity')
#Packing arguments với *
def test3(*args):
	print(args)
arr = (x for x in range(10))
test3(*arr)
#Packing arguments với **
def dicts(number ,number2)	:
	print('number :',number)
	print('number2:',number2)
dic = {'number':'one','number2':'two'}
dicts(**dic)