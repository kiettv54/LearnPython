a=[1,2,3,4,5,6,7,8,9,1]
# đếm số lần xuất hiện 1 phần tử
b=a.count(1)
print(b)
#tìm số
c=a.index(2)
print(c)
# tạo ra một bản sau và giống list contructer 
d=a.copy()
print(d)
#dọn dẹp list
e=a.clear()
print(e)
#cộng phần tử vào list
a.append([5,4])
print(a)
#Lấy từng phần tử vào list
a.extend([44,55])
print(a)
#thêm phần tử vào vị trí i  insert(<vị trí thêm>,<phần tử>)
a.insert(1,7)
print(a)
# bỏ đi phần tử trong list và lấy phần tử đã bỏ ra
ff=a.pop(3)
print(ff)
#xóa đi phần tử đầu tiên
ar=[1,2,4,4,5]
ar.remove(1)
print(ar)
#in ra danh sách đảo ngược lại
ar.reverse()
print(ar)
#sắp xếp danh sách trong list
ar.sort(reverse=False) # hoặc ar.sort(reverse=True) hoặc ar.sort()
print(ar)	
l1 = [1,3,4,6,7,5]
l2 = [4,5,6,7,8]
in_l1 = l1[::1]
in_l2 = l2[::1]
print(in_l1)
print(in_l2)