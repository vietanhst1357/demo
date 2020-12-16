import math
print("ax^2 + bx + c = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
delta = b*b - 4*a*c
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm!!")
        else:
            print("Phương trình vô nghiệm :>>")
    else:
        x = -c/b
        print("Phương trình có một nghiệm x = ", x)
else:
    if delta > 0:
        x1 = float((-b - math.sqrt(delta))/(2*a))
        x2 = float((-b + math.sqrt(delta))/(2*a))
        print("Phương trình có 2 nghiệm là x1 = ", x1 ,", x2 = ", x2)
    elif delta == 0:
        x = float(-b/(2*a))
        print("Phương trình có nghiệm kép x1 = x2 = ", x)
    else:
        print("Phương trình vô nghiệm :>>")
