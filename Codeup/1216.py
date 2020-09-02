n = list(map(int, input().split(" ")))
bf = n[1]-n[2]
if n[0] > bf:
    print('do not advertise')
elif n[0] < bf:
    print('advertise')
else:
    print('does not matter')
