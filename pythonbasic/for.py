set_ = [5,8,1,9,4]
s = 0
for value in set_:
	s += value
print("Sum :",s)

database = {'Baby': 'em bé','Son-in-law':'Con rể','Grandfather':'ông','Nephew':'cháu trai','neice':'cháu gái'}
for key,value in database.items():
	print(key,':',value)
#break
s = 'Hello world'
for x in s:
	if x == ' ':
		break
	else :
		print(x)
#continue
a = 'information technology'
for x in a:
	if x == ' ':
		continue
	else :
		print(x)
#for...else
for x in (1,2,3,4,5,6):
	print(x)
else:
	print('Done!')

#range với list,tuple,string
lis = ['Hello world']
length = len(lis)
for x in range(length):
	print(lis[x])
#Comprehension
#Cú pháp:[ output-expression for-statement optional-predicate ]
['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]] # bỏ trống optional-predicate
['How--KTEAMeducation', 'Chia--SẺfree']
#nếu không dùng comprehension
lis = []
for a,b,c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]:
	a=a.capitalize()
	b=b.upper()
	c=c.lower()
	lis.append('--'.join((a,b + c)))
print(lis)
b = ['Hoa','Thiên','Động']
c = list(enumerate(b))
print(c)