n =5 #int(input("Nhap n: "))
print("Ma tran vuong cap", n)
gt = 0; x = n; y = 0; b = 0; c = 1; d = n; f = n - 1; h = n - 1; k = 0; g = 1; r = n - 1; e = 0
a = [x for x in range(n)]

#Tạo ma trận vuông cấp n
for i in range(n):
    a[i] = [0] * n

for i in range(n):
    #Trái sang phải
    for j in range(y, x):
        a[b][j + y - b] = gt
        gt += 1
    b += 1; x -= 1; y += 1

    #Trên xuống
    for j in range(c, d):
        a[j][f] = gt
        gt += 1
    c += 1; d -= 1; f -= 1

    #Phải sang trái
    for j in range(k, h):
        a[h][h + k - j - 1] = gt
        gt += 1
    k += 1; h -= 1

    #Dưới lên
    for j in range(g, r):
        a[r + g - j - 1][e] = gt
        gt += 1
    g += 1; r -= 1; e += 1

#Thêm số 0 vào trước các số nhỏ hơn 10
for i in range(n):
    for j in range(n):
        if 0 <= a[i][j] < 10:
            a[i][j] = '0{}'.format(a[i][j])
    print(a[i])