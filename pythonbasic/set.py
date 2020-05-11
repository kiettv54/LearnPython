#Set là một container, tuy nhiên không được sử dụng nhiều bằng LIST hay TUPLE.

#Một Set gồm các yếu tố sau:

#Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
#Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
#Set không chứa nhiều hơn 1 phần tử trùng lặp
#Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do đó, bạn không thể chứa một set trong một set.
#không chứa set trong set
#trong set chứa dược tuple
#trong set không chứa list
#không thể tạo một empty set bằng {}
#contructer tao ra 1 set
#Bản chất set không quan tâm đến vị trí phần tử
set_1={1,2,3}
set_2={'hello world',59,'Ron'}
print(set_1)
print(type(set_1))
print(set_2)
set_3={value for value in range(3)}
print(set_3)
#contructer
set_4=set((4,5,6))

print(set_4)
#tự phân tách chuỗi 
set_5=set(('Hello World'))
print(set_5)
#trong contructer trùng nhau chỉ hiển thị 1 phần tử trùng
#Có thể tạo contructer empty với dấu () vi dụ set_6=set()
set_6=set((1,2,3,4,1,2))
print(set_6)
#toán tử set_6
#kiểm tra 1 có tồn tại trong set hay không. kết quả return true hoặc return false
#true
print(1 in {1,2,3})
print((1,2) in {(1,2),3} )
#trừ set
print({1,2,3,5} - {1,3})
#kết quả là set rỗng
print({1,2} - {1,2,3})
#toán tử & : phần tử trong set1 tồn tại trong set2.Kết quả trả về là giao của 2 set
print({1,2,3} & {1,4,5})
#toán tử hoặc
#lấy hết phần tử trong set giống như phép hợp
print({1,2,3} | {4,5})
#loại bở phần tử trùng nhau
print({1,2,3} ^ {1})
#kết quả tạo ra mọt set rỗng
set_7={1,2,3}
set_7.clear()
print(set_7)
#pop xóa đi phần tử đầu tiên
set_8={1,2,3}
set_8.pop()
print(set_8)
#remove xóa đi phần tử bất kì khi truyền giá trị phần tử
set_9={1,2,3,4}
set_9.remove(1)
print(set_9)
#loại bỏ giá trị value trong set và bỏ qua lỗi
set_10={1,2,3,4}
set_10.discard(2)
print(set_10)
#copy sao chép set
set_11=set_10.copy()
print(set_11)
#add thêm phần tử vào set.lưu ý không thể thêm phần tử trùng lập đã có trong set
set_11.add(5)
print(set_11)
#địa chỉ của id không thay đổi khi add giá trị vào set
print(id(set_11))
set_11.add(6)
print(id(set_11))
