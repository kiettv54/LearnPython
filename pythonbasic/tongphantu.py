n = 10#int(input("nhap n:"))
list1 = [x for x in range(n)]
list2 = [x for x in list1 if x != max(list1)]
print(max(list2))
