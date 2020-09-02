n = list(map(int, input().split()))
c = 0
for i in range(len(n)):
    if n[i] <=170:
        c = 1
        print('CRASH %d'%n[i])
        break
if c == 0:
    print('PASS')
