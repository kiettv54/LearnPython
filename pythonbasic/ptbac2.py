import math
a=float(input('enter a:'))
b=float(input('enter b:'))
c=float(input('enter c:'))
delta = (b * b) - (4 * a * c)
if delta > 0:
# Khối lệnh mới, thụt vào đầu dòng
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print ("Phuong trinh co hai nghiem phan biet:")
    print ("x1 = ", x1, "; ", "x2 = ", x2)
elif delta < 0:
    print('phuong trinh vo nghiem')
elif delta >0:
    x1=x2=-b/(2*a)
    print ("x1 = ", x1, "; ", "x2 = ", x2)
