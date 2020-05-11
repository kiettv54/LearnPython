#r:Mở để đọc.Đây là mode mặc định
#r+:Mở để đọc và ghi
#w:Mở để ghi.Trước đo xóa hết nội dung file hiện có.Nếu file không tồn tại sẽ tạo một file mới với tên file ta trùng vào
#w+:Mở để đọc và ghi.Trước đo xóa hết nội dung file hiện có.Nếu file không tồn tại sẽ tạo một file mới với tên file ta trùng vào
#a: mở để ghi.Nếu file không tồn tại sẽ tạo một file mới với tên ta truyền vào
##a+: mở để đọc và ghi.Nếu file không tồn tại sẽ tạo một file mới với tên ta truyền vào

#mở file
file_open= open('text.txt')

#phương thức read .Cú pháp <file>.read(size=-1)  
#Công dụng: Nếu size bị bỏ trống hoặc là một số âm. Nó sẽ đọc hết nội dung của file đồng thời đưa con trỏ file tới cuối file
#. Nếu không nó sẽ đọc tới n kí tự (với n = size) hoặc cho tới khi nội dung của file đã đọc xong.
#	Sau khi đọc được nội dung, nó sẽ trả về dưới một dạng chuỗi.
#	Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng 0
data = file_open.read()
print('đọc dữ liệu có trong file:',data) 
file_open.close()
#đọc từng kí tự
file_open= open('text.txt')

data1 = file_open.read(1)
print('Đọc các ký tự khi cho số ký tự:',data1)
file_open.close()
# Phương thức readline Cú pháp:<File>.readline(size=-1)
# Công dụng: Với parameter size thì hoàn toàn tương tự như phương thức read.
"""Khác biệt ở chỗ, phương thức readline chỉ đọc một dòng có nghĩa là đọc tới khi nào gặp newline hoặc hết file thì ngừng.
Con trỏ file cũng sẽ đi từ dòng này qua dòng khác.
Kết quả đọc được trả về dưới dạng một chuỗi.
Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng"""
file_op=open('text.txt')
data2= file_op.readline()
print('Phương thức readline,đọc 1 dòng:',data2)
file_op.close()
#phương thức readlines
"""Cú pháp:<File>.readlines(hint=-1)
Ở mức độ cơ bản, ta không phải quan tâm đến parameter hint.
 Công dụng: Phương thức này sẽ đọc toàn bộ file, sau đó cho chúng vào một list. Với các phần tử trong list là mỗi dòng của file.
		Con trỏ file sẽ được đưa  tới cuối file. Khi đó, nếu bạn tiếp tục dùng readlines. Bạn sẽ nhận được một list rỗng."""
file_op=open('text.txt')
data=file_op.readlines()
print('Phương thức readlines,đọc tất cả:',data)
#Đọc file bằng constructor nhận iterable
#đọc file từ list
file_object = open('text.txt')
data = list(file_object)
file_object.close()
print('Contructor list:',data)
#đọc file từ tuple
file_object = open('text.txt')
data = tuple(file_object)
file_object.close()
print('Contructor tuple:',data)
#ghi dữ liệu vào file
file_object = open('text.txt',mode = 'a+')
data = file_object.write('\nhay trao cho anh \n')
file_object.close()
#Kiểm soát con trỏ file
#Phương thức seek
"""Công dụng: Phương thức này giúp ta di chuyển con trỏ từ vị trí đầu file qua offset kí tự. Và parameter offset phải là một số tự nhiên.
		Nhờ phương thức này, ta có thể ghi nội dung từ bất cứ đâu trong file.
		Và từ đó ta có thể đọc lại file sau khi ta đưa con trỏ file xuống cuối file."""
print('Phương thức seek:')
file_object = open('text.txt',mode='r')
data = file_object.read()
#dịch chuyển con trỏ về vị trí đầu chuỗi
data = file_object.seek(0)
data2= file_object.read()
file_object.close()
#Câu lệnh with
#Cấu trúc cơ bản của câu lệnh with là
#with expression [as variable]:
#	with-block    
"""Nhớ rằng with-block nằm thụt vào so với dòng with expression (theo chuẩn PEP8 là 4 space và là dùng space không dùng tab)
	Câu lệnh này liên quan đến phương thức __enter__ và __exit__ của đối tượng. Do đó, ở đây Kteam sẽ nói cơ bản khi sử dụng file.
	Đặc điểm của câu lệnh with khi sử dụng với file là. Khi kết thúc with-block. File sẽ được đóng."""
with open('D:\python\pythonbasic\text.txt') as fopen:
	data = fopen.read()
print('Phương thức with:',data)