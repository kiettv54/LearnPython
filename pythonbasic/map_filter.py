'''Hàm map này có tác dụng duyệt qua tất cả các phần tử của một hoặc nhiều list, dictionary hoặc tương tự như thế, sử dụng đơn giản với cú pháp như sau:

map(function, iterable1, iterable2 ,...)
Trong đó:

function là hàm xử lý logic qua mỗi lần lặp giá trị trong interable1, ......
interable1, interable2 là các list, dict ,... các bạn cần lặp.
Hàm map sẽ trả về một map object chứa các kết quả sau khi thực thi.'''
def matrix(a):
	return a*a
result = map(matrix,[1,2,3,4])
print(list(result))
#Và function kia bạn có thể khai báo dưới dạng lambla cho gọn như sau:

result = map(lambda x: x * x, [1, 2, 3, 4])

print(list(result))  # [1, 4, 9, 16]
#VD: map đối với 2 list truyền vào.

result = map(lambda x, y: x + " " + y, ['red', 'blue'], ['green', 'black'])

print(list(result))  # ['red green', 'blue black']
