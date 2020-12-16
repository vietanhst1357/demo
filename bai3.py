temp = int( input('Nhap so a: '))
if temp >=100:
    print('Stay at home and enjoy a movie')
elif temp>=92:
    print('Stay at home')
elif temp==75:
    print('Go outside and enjoy the weather')
elif temp<0:
    print("It's cold outside")
else:
    print("Let's go to school")