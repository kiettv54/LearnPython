'''Iteration là một khái niệm chung cho việc lấy từng phần tử một của một đối tượng nào đó,
 bất cứ khi nào bạn sử dụng vòng lặp hay kĩ thuật nào đó để có được giá trị một nhóm phần tử thì đó chính là Iteration.
Ví dụ: như bạn ăn một snack, bạn sẽ lấy từng miếng trong bọc snack ra ăn cho tới khi hết thì thôi. 
Bạn có thể coi việc lấy bánh là một vòng lặp. Đương nhiên bạn cũng có thể chọn không lấy hết số bánh ra.'''

"""Iterator object đơn giản chỉ là một đối tượng mà cho phép ta lấy từng giá trị một của nó. 
Có nghĩa là bạn không thể lấy bất kì giá trị nào như ta hay làm với List hay Chuỗi.
Iterator không có khả năng tái sử dụng trừ một số iterator có phương thức hỗ trợ như file object sẽ có phương thức seek.
Iterator sử dụng hàm next để lấy từng giá trị một. Và sẽ có lỗi StopIteration khi bạn sử dụng hàm next lên đối tượng đó trong khi nó hết giá trị đưa ra cho bạn.
Các iterable object chưa phải là iterator. Khi sử dụng hàm iter sẽ trả về một iterator. Đây cũng chính là cách các vòng lặp hoạt động."""
#vidu:
a = [x for x in range(3)]
print(a)
 # sử dụng () cho ra một generator expression – một iterator
 # lấy ra một phần tử
b = (x for x in range(3))
print(next(b))
print(next(b))
print(next(b))
#list
#interable không hỗ trợ kiểu indexing ví dụ: print(inter_list[0]) sẽ bị lỗi
ls = [1,2,3,4,'hello world',5,[6,7,8]]
inter_list = iter(ls)
print(inter_list)
print(next(inter_list))
#Hàm toán tử
#max cú pháp:max(iterable, *[, default=obj, key=func]).default là giá trị trả về khi không lấy được giá trị nào
lis = [1,4,3,2,6,5]
a=max(lis)
print('Max:',a)
# min
a = min(lis)
print('Min:',a)
#sum
a = sum(lis)
print('sum:',a)
#sorted mặc định sắp xếp tăng dần
sort_a = sorted(lis)
print('sort up:',sort_a)
#sorted giảm dần
sort_b = sorted(lis,reverse = True)
print('Sort down:',sort_b)

