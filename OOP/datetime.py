n = int(input("nhap so luong phan tu:"))
list1 = [float(input("Nhap phan tu thu nhat "+str(i+1)+" : ")) for i in range(n)]
try:
    list2 = [x for x in list1 if x != max(list1)]
    print('so lon thu hai la:',int(max(list2)))
except ValueError:
    print('cac phan tu trong mang bang nhau')

