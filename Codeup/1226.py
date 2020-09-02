l = list(map(int, input().split(' ')))
j = list(map(int, input().split(' ')))
c = 0
s = 0
for i in range(len(l[:-1])):
    for k in range(len(j)):
        if l[i] == j[k]:
            c = c + 1
if c == 6:
    print('1')
elif c == 5:
    for p in range(len(j)):
        if l[-1] == j[p]:
            s = 1
    if s == 1:
        print('2')
    else:
        print('3')
elif c == 4:
    print('4')
elif c == 3:
    print('5')
else:
    print('0')
