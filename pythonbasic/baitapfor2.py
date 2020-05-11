#Sử dụng sequence scan để thay đổi phần tử đầu tiên của mỗi phần tử trong List dưới đây thành None
lis =[[1,2,3],[4,5,6]]
for value in range(len(lis)):
	lis[value][0] =None
print(lis) 
