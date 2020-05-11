#được giới hạn bởi cặp ngoặc ()
#Các phần tử của tuble được phân cách bởi dấu phẩy "," 
#tuble có khả năng chứa mọi giá trị
#tốc độ truy xuất của tuble nhanh hơn list
#dung lượng chiếm trong bộ nhớ nhỏ hơn list
#bảo vệ dữ liệu của bạn sẽ không bị thay đổi
# có thể dùng lạm key của dictionnary
# #---tương tự như list----------------------------------------------
tup =(1,2,(3,4),5,'kiet',6)
print(tup)
a= tuple ((1,2,4))
print(a)
tupl=(i for i in range(10))
b=tuple(tupl)
print(b)
# Toán tử
#Cộng
tupp = (1,2,3)
tupp +=(4,5,6)
print('plus tuple:',tupp)
# nhân với một số
tupp *=2
print('Nhân tuple:',tupp)
#toán tử kiểm tra có phần tử trong tuple hay trong
test=2 in tupp
print(' 2 :',test)
#truy xuất phần tử trong tuple
ptu=tupp[2]
print('truy xuất phần tử:',ptu)
#lấy độ dài tuple
lentuple=len(tupp)
print('Độ dài tuple:',lentuple)
#lấy phần tử trong tuple bẳng 1 trong 2 câu lệnh
#tupp[len(tupp)-1] hoặc tupp[-1] hoặc tupp[:-1] (lấy đi phần tử trừ đi phần tử cuối)
getnum=tupp[-1]
print('Num of tuple:',getnum)
#đảo ngược tuple với cấu trúc tupp[::-1]
swap=tupp[:: -1]
print('tuple đảo ngược:',swap)
#ma trận tuple
tupmatrix=((1,2,3),(4,5,6))
print(tupmatrix[1][1])
##Só lần xuât hiện của phần tử
timenum=tupp.count(1)
print('số lần xuất hiện của một phần tử:',timenum)
#tìm vị trí xuất hiện của phần tử
findnum=tupp.index(4)
print('vị trí xuất hiện:',findnum)
b={}
b[0] = 3
print(b)
liss = [1,2,3,4]
tublee = list(liss)
print(tublee)