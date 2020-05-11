'''Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
 Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.'''
arr = []
for value in range(2000,3201):
	if (value % 7 == 0) and (value % 5 != 0):
		arr.append(str(value))
print(','.join(arr))
'''Viết một chương trình có thể tính giai thừa của một số cho trước.
 Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.'''
n = 8
x = 1
if (n == 0) :
	print(n,'!=',x)
else :
	for value in range(n+1):
		if value !=0:
			x *= value
	print(n,'!=',x)
#Cho một danh sách viết chương trình ỉn ra vị trí 2 số cộng lại bằng số đã cho
#Thuật toán phức tạp 0(n*n)



def TwoSum(*arg,tanger):
	len_lis = len(arg)
	for value in range(len_lis -1):
		value2 = value +1
		for value2 in range(len_lis):
			if (arg[value] + arg[value2]) == tanger:
				return [value,value2]
	return []
lis = [2,7,11,15]
#print(TwoSum(*lis,tanger =18))

