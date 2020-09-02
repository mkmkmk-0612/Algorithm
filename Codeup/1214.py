y, m = input().split()
y = int(y)
m = int(m)
if y%400 == 0: #윤년
   if m<8:
       if m ==2:
           print('29')
       elif m%2 ==1:
           print('31')
       else:
           print('30')
   else:
       if m==2:
           print('29')
       elif m%2 ==0:
           print('31')
       else:
           print('30')
elif y%4 == 0 and y%100!=0: #윤년
    if m < 8:
        if m == 2:
            print('29')
        elif m % 2 == 1:
            print('31')
        else:
            print('30')
    else:
        if m == 2:
            print('29')
        elif m % 2 == 0:
            print('31')
        else:
            print('30')
else: #윤년 아님
    if m < 8:
        if m == 2:
            print('28')
        elif m % 2 == 1:
            print('31')
        else:
            print('30')
    else:
        if m == 2:
            print('28')
        elif m % 2 == 0:
            print('31')
        else:
            print('30')

