#Dict(Dictionary) cũng là một container như LIST, TUPLE. 
#Có điều khác biệt là những container như List, Tuple có các index để phân biệt các phần tử thì Dict dùng các key để phân biệt.

#Chắc bạn cũng dùng từ điển tiếng Anh để tra từ vựng rồi nhỉ? Có rất nhiều từ vựng trong đó nhưng mà không từ vựng nào giống nhau.
# Có chăng chúng chỉ giống nhau về nghĩa? Và đó cũng như Dict(Dictionary) hoạt động trong Python

#Một Dict gồm các yếu tố sau:

#Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
#Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
#Các phần tử của Dict phải là một cặp key-value
#Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
#Các key buộc phải là một hash object
#Cú pháp:{<key_1: value_1>, <key_2: value_2>, .., <key_n: value_n>},
dic = {'sex':'giới tính,tình dục','baby':'em bé','home':'nhà'}
for word in dic :
	print(word,':',dic[word])
#khởi tạo dict rỗng(contructor)
dic1=dict()
print(dic1)
#khởi tạo dict compreshension(code không tối ưu)
dic2 = {key: value for key, value in [('name', 'Kteam'), ('member', 69)]}
print(dic2)
#khởi tạo dict mapping
class Map_Class:
	def keys(self):
		return [1, 2, 3]
	def __getitem__(self, key):
		return key * 2
map_obj = Map_Class()
dic3 = dict(map_obj)
print(dic3)
#Khởi tạo bằng iterable
iter_ = [('name', 'Kteam'), ('member', 69)]
dic4 = dict(iter_)
print(dic4)
#Khởi tạo bằng keyword arguments
#Cứ hiểu đơn giản là giống như việc bạn khởi tạo biến và giá trị rồi đưa cho dict đó giữ giùm.
#Một lưu ý là những biến này không bị ảnh hưởng hoặc ảnh hưởng gì đến các biến bên ngoài
name = 'SpaceX'
member = 696969
dic5 = dict(name='Kteam', member=69)
print(dic5)
print(name)
print(member)
#Sử dụng Phương thức fromkeys
# Cách này cho phép ta khởi tạo một dict với các keys nằm trong một iterable. Các giá trị này đều sẽ nhận được một giá  trị với mặc định là None
iter_ = ('name', 'number')
dic_none = dict.fromkeys(iter_)
print(dic_none)
dic6 = dict.fromkeys(iter_, 'non None value')
print(dic6)

#các thao tác khác
#copy
d=dic.copy()
#Xóa
a={'1':1,"2":2}
a.clear()
#lấy phần tử
a={'1':1,"2":2}
value=a.get('1')
# chuyển dict về list
database = {'Baby': 'em bé','Son-in-law':'Con rể','Grandfather':'ông','Nephew':'cháu trai','neice':'cháu gái'}
db = list(database.items())
print(db)