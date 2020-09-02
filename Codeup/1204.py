n = int(input())

a = n//10
b = n%10
if a==0:
    if b == 1:
        print('%dst' %n)
    elif b == 2:
        print('%dnd' %n)
    elif b == 3:
        print('%drd' %n)
    else:
        print('%dth' %n)
elif a == 1:
    print('%dth'%n)
else:
    if b == 1:
        print('%dst'%n)
    elif b == 2:
        print('%dnd'%n)
    elif b == 3:
        print('%drd' %n)
    else:
        print('%dth' %n)
