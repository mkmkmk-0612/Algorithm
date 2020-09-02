a, b = input().split()
a = int(a)
b = int(b)
cal = 0
if a == 1:
    cal = cal + 400
elif a == 2:
    cal = cal + 340
elif a == 3:
    cal = cal + 170
elif a == 4:
    cal = cal + 100
elif a == 5:
    cal = cal + 70

if b == 1:
    cal = cal + 400
elif b == 2:
    cal = cal + 340
elif b == 3:
    cal = cal + 170
elif b == 4:
    cal = cal + 100
elif b == 5:
    cal = cal + 70

if cal > 500:
    print('angry')
else:
    print('no angry')

