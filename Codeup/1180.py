n = int(input())
if n >= 10:
    if str(n)[-1] == '0':
        n = 2*int(str(n)[0])
    else:
        n = 2*(10*(int(str(n)[-1])) + int(str(n)[0]))
    if n >= 100:
        n = n - 100
    print(n)
    if n <= 50:
        print('GOOD')
    else:
        print('OH MY GOD')
else:
        n = 2*n
        print(n)
        if n <= 50:
            print('GOOD')
        else:
            print('OH MY GOD')
