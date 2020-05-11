# hashtable
# unhashtable
# #cú pháp id(<dữ liệu>)
# kết quả trả về là kiểu int,là 1 giá trị truyền vào và giá trị không thay đổi suốt chương trình
# <địa chỉ>|<giá trị>
a= id(5)
#so sánh a và b ta thấy kết qquar trả về địa chỉ khác nhau
b=5
c=id(b)
print(a)
print('băm:',hash(a))
print(c)
# thêm một đơn vị
n=69
print(n)
# 2 hàm tương tự nhau
# Cộng
print(n+1)
print(n.__add__(1))
#trừ
print(n-1)
print(n.__sub__(1))
#nhân
print(n*2)
print(n.__mul__(2))
#hàm chuyển dấu
print(-n)
print(n.__neg__())
#Cộng thêm , hai toán tử tương đương nhau
s1=(1,2)
s1.append(3)
s1+=(3)
