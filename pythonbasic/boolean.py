inp1=3
inp2=5
print(inp1>inp2)
print(inp1 != inp2)
print(inp1 == inp2)
#ord
or1=ord('a')
or2=ord('A')
print(or1)
print(or2)
print('aaa' < 'aaaBB')
#toán tử is
#is khác với ==
#== là so sánh giá trị
#is dùng để diễn giải, định nghĩa 

lis = [1,2,3]
lis_ = [1,2,3]
print(lis == lis_)
print(lis is lis_)
#kết luận khi so sánh . toán tử == lấy giá trị value để so sánh
#toán tử is lấy giá trị hàm id để so sánh 
lis= lis_
print(lis is lis_)
#And
print(6 >5 and 3<4)
#or
print(4>3 or 3==1)
#not
print(not 4>3)
#bool
"""Mọi giá trị khi chuyển về Boolean đều là True trừ một số trường hợp sau
Số 0
None
Rỗng"""
print(bool(0))
print(bool(3))
#Syntaxnic sugar 
a=3
print(1 < a < 5)