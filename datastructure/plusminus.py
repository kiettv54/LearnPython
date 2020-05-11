from decimal import *
arr = [1, 1, -1, -1, 0, 0]
s1 = 0
s2 = 0
s3 = 0
lenght = len(arr)
for x in arr:
    if x > 0:
        s1 += 1
    elif x < 0:
        s2 += 1
    else:
        s3 += 1
lenght = float(lenght)

b = [Decimal(s1)/Decimal(lenght) , s2/lenght, s3/lenght]
print(b)
