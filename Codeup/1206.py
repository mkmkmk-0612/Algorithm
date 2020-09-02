a, b = input().split(' ')
a = int(a)
b = int(b)
if b%a == 0:
    print('%d*%d=%d'%(a,b/a,b))
elif a%b == 0:
    print('%d*%d=%d' % (a, a /b, b))
else:
    print('none')
