n = list(map(int,input().split()))
c = 0
while n[0] < 90:
    c = c + 1
    n[0] = n[0] + 5
if n[2] > n[1] + c:
    print('lose')
elif n[2] < n[1] + c:
    print('win')
else:
    print('same')
